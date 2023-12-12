import requests



class Service:

    def __init__(self, id: int, name:str, price:float, is_available:bool):
        self.id = id
        self.name = name
        self.price = price
        self.is_available = is_available 

    def __repr__(self):
        return '<Service "%s">' % self.name

class Number:

    def __init__(
        self,
        order_id: str,
        number: str, 
        remaining_seconds: int,
        api,
        carrier: str=None, 
        city: str=None,
        region: str=None,
        area_code: str=None
    ):
        self.api = api
        self.order_id = order_id
        self.number = number
        self.carrier = carrier
        self.city = city 
        self.region = city 
        self.area_code = city 
        self.remaining_seconds = remaining_seconds 

    def check_sms(self):
        return self.api.check_sms(self.order_id,self.number)

class Sms:
    def __init__(
        self,
        order_id: str,
        state: str,
        msg: str, 
        remaining_seconds: int,
        api,
        sms_content: str=None, 
        sms_received_at: str=None,
        code: str=None,
    ):
        self.api = api
        self.order_id = order_id
        self.state = state
        self.msg = msg
        self.remaining_seconds = remaining_seconds 
        self.sms_content = sms_content 
        self.sms_received_at = sms_received_at 
        self.code = code 
    
    def get_code(self):
        if self.code is None:
            return None
        else:
            return self.code




class SmsRed:
    def __init__(self,token: str):
        self.token = token
        self.header = {
            'content-type':'application/x-www-form-urlencoded',
            'X-API-KEY':token
        }
        self.list_of_service = []
        self.services_state()

    def services_state(self):
        r = requests.get(
            'https://sms.red/services_state',
            headers = self.header
        ) 
        for i in r.json():
            if i['id'] == 106:
                i['price_per_code'] = 2
            elif i['id'] == 1000:
                i['price_per_code'] = 1.5
            else:
                i['price_per_code'] = 1.25
            self.list_of_service.append(
                Service(
                    i['id'],
                    i['name'],
                    i['price_per_code'],
                    i['is_available']
                )
            )

    def order_number(self,service_id: int,**kwargs):
        kwargs['service_id'] = service_id
        r = requests.post(
            'https://sms.red/order_number',
            headers = self.header,
            data = kwargs
        ).json()
        return Number(
            r['order_id'],
            r['number'],
            r.get('remaining_seconds'),
            self,
            r['carrier'],
            r['city'],
            r['region'],
            r['area_code']
        )

    def check_sms(self,order_id,number):
        data = {
            'order_id': order_id,
            'number': number
        }
        r = requests.post(
            'https://sms.red/check_sms',
            headers = self.header,
            data = data
        ).json()
        if r['state'] == 'WAITING_FOR_SMS':
            return Sms(
                order_id,
                r['state'],
                r['msg'], 
                r.get('remaining_seconds'),
                self
            )
        elif r['state'] == 'SMS_RECEIVED':
            return Sms(
                order_id,
                r['state'],
                r['msg'], 
                r.get('remaining_seconds'),
                self,
                r['sms_content'],
                r['sms_received_at'],
                r['code']
            )
        


# obj = SmsRed('49edeb591eb489d1fdfa4e6f7875a5ba0a506d39')
# print(obj.order_number(obj.list_of_service[0].id).number)


# r = requests.post('https://httpbin.org/post', data = data_dict,headers =header)