from flask import Flask, request, render_template
from urllib.parse import parse_qs

from paykassa.dto import CheckTransactionRequest, CheckPaymentRequest
from paykassa.merchant import MerchantApi

from config import pk_data
from databases import Transactions, User
from mics import Session

app = Flask(__name__)
pk = MerchantApi(pk_data[0], pk_data[1])

@app.route('/confirm', methods=['GET', 'POST'])
def confirm():
    if request.method == 'POST':
        data = request.get_data(as_text=True)
        parsed_data = parse_qs(data)
        processed_data = {k: v[0] for k, v in parsed_data.items()}

        if processed_data['type'] == 'sci_confirm_order':

            session = Session()
            transaction = session.query(Transactions).filter_by(invoice_id=processed_data["order_id"]).all()

            request_check = CheckPaymentRequest() \
                .set_private_hash(private_hash=processed_data['private_hash'])

            response_check = pk.check_payment(request_check)
            if 'successfully' in response_check.get_message():
                user = session.query(User).filter_by(id=transaction.user_id).first()
                session.query(Transactions).filter_by(user_id=transaction.user_id).filter_by(
                    status='unpaid'
                ).update({"status": "paid"})
                session.query(User).filter_by(id=transaction.user_id).update(
                    {"balance": float(user.balance) + float(response_check.get_amount())}
                )
                session.commit()

            return f'{processed_data["order_id"]}|success', 200
        else:
            return 'ok', 200
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=False, port=80, host='0.0.0.0')
