from aiogram.types import (
    ReplyKeyboardRemove,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    WebAppInfo
)
from config import single_products

def language_keyboard():
    result = InlineKeyboardMarkup()
    result.row(InlineKeyboardButton("🇷🇺 Русский", callback_data="lang~ru"))
    result.row(InlineKeyboardButton("🇺🇸 Английский", callback_data="lang~en"))
    return result


def markup_start(lang):
    result = ReplyKeyboardMarkup(resize_keyboard=True)
    if lang == "ru":
        buttons = [
            "📈 Каталог",
            "🎟 Bus Info",
            "👥 Аккаунты",
            "🛒 Мой Профиль",
            "📎 FAQ",
            "💬 Поддержка",
            # "✉️SMS",
            "🇺🇸 English",
        ]
    else:
        buttons = [
            "📈 Catalog",
            "🎟 Bus Info",
            "👥 Accounts",
            "🛒 My profile",
            "📎 FAQ",
            "💬 Support",
            # "✉️SMS",
            "🇷🇺 Русский",
        ]
    result.row(buttons[0])
    result.row(buttons[1])
    result.row(buttons[2])
    result.row(buttons[3], buttons[4])
    result.row(buttons[5])
    result.row(buttons[6])
    return result


def single_catalog_list(product_list, key="single_product"):
    result = InlineKeyboardMarkup()
    for i in product_list:
        if i.is_sold == False or i.is_sold == None:
            result.row(InlineKeyboardButton(f"{i.name} - {i.price}$", callback_data=f"{key}~{i.id}"))
        # else:
        #     result.row(InlineKeyboardButton(f'{i.name} - {i.count} - {i.price}$',callback_data = f'single_product~{None}'))
    return result


def get_full_message_keyboard(lang):
    result = InlineKeyboardMarkup()
    if lang == "ru":
        buttons = ["Получить полное сообщение"]
    else:
        buttons = ["Get full message"]
    result.row(InlineKeyboardButton(f"{buttons[0]}", callback_data=f"get_full_message"))
    return result


def get_list_of_service_tru(ls):
    result = InlineKeyboardMarkup()
    for ind, i in enumerate(ls):
        result.row(InlineKeyboardButton(f"{i}-1$", callback_data=f"sms_service_tru~{ind}"))
    return result


def get_list_of_service(ls, pages=[], number=0):
    result = InlineKeyboardMarkup()
    if pages == []:
        page = []
        for i in ls:
            print(i.id, i.name)
            page.append(i)
            if len(page) > 20:
                pages.append(page)
                page = []

    for i in pages[number]:
        result.row(InlineKeyboardButton(f"{i.name}-{i.price}$", callback_data=f"sms_service~{i.id}"))
    if number == 0:
        result.row(
            InlineKeyboardButton("<<", callback_data=f"page~{len(pages)-1}"),
            InlineKeyboardButton(f"{number+1}/{len(pages)}", callback_data=f"pages"),
            InlineKeyboardButton(">>", callback_data=f"page~{1}"),
        )
    elif number == len(pages) - 1:
        result.row(
            InlineKeyboardButton("<<", callback_data=f"page~{len(pages)-2}"),
            InlineKeyboardButton(f"{number+1}/{len(pages)}", callback_data=f"pages"),
            InlineKeyboardButton(">>", callback_data=f"page~{0}"),
        )
    else:
        result.row(
            InlineKeyboardButton("<<", callback_data=f"page~{number-1}"),
            InlineKeyboardButton(f"{number+1}/{len(pages)}", callback_data=f"pages"),
            InlineKeyboardButton(">>", callback_data=f"page~{number+1}"),
        )
    return result, pages


def get_mobile_operator(loc):
    result = InlineKeyboardMarkup()
    if loc == "ru":
        buttons = ["T-mobile"]
    else:
        buttons = ["T-mobile"]
    result.row(InlineKeyboardButton(f"{buttons[0]}", callback_data=f"operator~t-mobile"))
    #     result.row(InlineKeyboardButton(f'{buttons[1]}',callback_data = 'operator~other'))
    return result


def order_process(loc, order_id):
    result = InlineKeyboardMarkup()
    if loc == "ru":
        buttons = ["Проверить смс", "Назад"]
    else:
        buttons = ["Check SMS", "Back"]
    result.row(InlineKeyboardButton(f"{buttons[0]}", callback_data=f"check_sms~{order_id}"))
    result.row(InlineKeyboardButton(f"{buttons[1]}", callback_data="back_to_menu"))
    return result


def catalog_list(product_list):
    result = InlineKeyboardMarkup()
    for i in product_list:
        if i.count != 0:
            result.row(
                InlineKeyboardButton(
                    f"{i.name} - {i.count} - {i.price}$",
                    callback_data=f"product~{i.id}",
                )
            )
        else:
            result.row(
                InlineKeyboardButton(
                    f"{i.name} - {i.count} - {i.price}$",
                    callback_data=f"product~{None}",
                )
            )
    return result


def admin_catalog_list(product_list):
    result = InlineKeyboardMarkup()
    for i in product_list:
        result.row(InlineKeyboardButton(f"{i.name} - {i.count} - {i.price}$", callback_data=f"product~{i.id}"))
    return result


def buy_keyboard(loc):
    result = InlineKeyboardMarkup()
    if loc == "ru":
        buttons = ["Купить", "❌ Отмена"]
    else:
        buttons = ["Buy", "❌ Cancel"]
    result.row(InlineKeyboardButton(f"{buttons[0]}", callback_data=f"buy"))
    result.row(InlineKeyboardButton(f"{buttons[1]}", callback_data="dispose"))
    return result


def admin_add_single_product_category(types):
    result = InlineKeyboardMarkup()
    for i in single_products:
        result.row(InlineKeyboardButton(f"{i}", callback_data=f"single_add~{i}"))
    return result


def order_ok(loc):
    result = InlineKeyboardMarkup()
    if loc == "ru":
        buttons = ["Подтвердить покупку", "❌ Отмена"]
    else:
        buttons = ["Buy", "❌ Cancel"]
    result.row(InlineKeyboardButton(f"{buttons[0]}", callback_data=f"order_ok"))
    result.row(InlineKeyboardButton(f"{buttons[1]}", callback_data="dispose"))
    return result


def my_cabinet(loc):
    result = InlineKeyboardMarkup()
    if loc == "ru":
        buttons = ["🤑Пополнить баланс", "🛒Покупки", "❌ Отмена"]
    else:
        buttons = ["🤑Add balance", "🛒Orders", "❌ Cancel"]
    result.row(InlineKeyboardButton(f"{buttons[0]}", callback_data="add_balance"))
    result.row(InlineKeyboardButton(f"{buttons[1]}", callback_data="orders"))
    result.row(InlineKeyboardButton(f"{buttons[2]}", callback_data="dispose"))
    return result


def await_add_balance(loc):
    result = InlineKeyboardMarkup()
    if loc == "ru":
        buttons = ["🤑Пополнить баланс"]
    else:
        buttons = ["🤑Add balance"]
    result.row(InlineKeyboardButton(f"{buttons[0]}", callback_data="add_balance"))
    # result.row(InlineKeyboardButton(f'{buttons[1]}',callback_data = 'orders'))
    return result


def deposit_keyboard(loc, link, payment_id):
    result = InlineKeyboardMarkup()
    if loc == "ru":
        buttons = ["Ссылка", "Проверить оплату", "❌ Отмена"]
    else:
        buttons = ["Payment page", "Check payment", "❌ Cancel"]
    result.row(
        InlineKeyboardButton(f"{buttons[0]}", url=link),
        InlineKeyboardButton(f"{buttons[1]}", callback_data=f"p~{payment_id}"),
    )
    result.row(InlineKeyboardButton(f"{buttons[2]}", callback_data="dispose"))
    return result


def deposit_cryptobot_keyboard(loc, link, payment_id):
    result = InlineKeyboardMarkup()
    if loc == "ru":
        buttons = ["Ссылка", "Проверить оплату", "❌ Отмена"]
    else:
        buttons = ["Payment page", "Check payment", "❌ Cancel"]
    result.row(
        InlineKeyboardButton(f"{buttons[0]}", url=link),
        InlineKeyboardButton(f"{buttons[1]}", callback_data=f"p_cryptobot~{payment_id}"),
    )
    result.row(InlineKeyboardButton(f"{buttons[2]}", callback_data="dispose"))
    return result


def deposit_btcpay_keyboard(loc, link, payment_id):
    result = InlineKeyboardMarkup()
    if loc == "ru":
        buttons = ["Ссылка", "Проверить оплату", "❌ Отмена"]
    else:
        buttons = ["Payment page", "Check payment", "❌ Cancel"]
    result.row(
        InlineKeyboardButton(f"{buttons[0]}", url=link),
        # InlineKeyboardButton(f"{buttons[1]}", callback_data=f"p_btcpay~{payment_id}"),
    )
    result.row(InlineKeyboardButton(f"{buttons[2]}", callback_data="dispose"))
    return result

def deposit_paykassa_keyboard(loc, link):
    result = InlineKeyboardMarkup()
    if loc == "ru":
        buttons = ["Оплатить", "Проверить оплату", "❌ Отмена"]
    else:
        buttons = ["Pay", "Check payment", "❌ Cancel"]
    result.row(
        InlineKeyboardButton(f"{buttons[0]}", web_app=WebAppInfo(url=link))
    )
    result.row(InlineKeyboardButton(f"{buttons[2]}", callback_data="dispose"))
    return result


def deposit_ltcpay_keyboard(loc, link, payment_id):
    result = InlineKeyboardMarkup()
    if loc == "ru":
        buttons = ["Ссылка", "Проверить оплату", "❌ Отмена"]
    else:
        buttons = ["Payment page", "Check payment", "❌ Cancel"]
    result.row(
        InlineKeyboardButton(f"{buttons[0]}", url=link),
        # InlineKeyboardButton(f"{buttons[1]}", callback_data=f"p_ltcpay~{payment_id}"),
    )
    result.row(InlineKeyboardButton(f"{buttons[2]}", callback_data="dispose"))
    return result


def deposit_qiwi_keyboard(loc, link, payment_id):
    result = InlineKeyboardMarkup()
    if loc == "ru":
        buttons = ["Ссылка", "Проверить оплату", "❌ Отмена"]
    else:
        buttons = ["Payment page", "Check payment", "❌ Cancel"]
    result.row(
        InlineKeyboardButton(f"{buttons[0]}", url=link),
        # InlineKeyboardButton(f"{buttons[1]}", callback_data=f"p_qiwi~{payment_id}"),
    )
    result.row(InlineKeyboardButton(f"{buttons[2]}", callback_data="dispose"))
    return result


def deposit_perfectmoney_keyboard(loc, payment_id):
    result = InlineKeyboardMarkup()
    if loc == "ru":
        buttons = ["Проверить оплату", "❌ Отмена"]
    else:
        buttons = ["Check payment", "❌ Cancel"]
    # result.row(
    #     InlineKeyboardButton(f"{buttons[0]}", callback_data=f"p_pm~{payment_id}")
    # )
    result.row(InlineKeyboardButton(f"{buttons[1]}", callback_data="dispose"))
    return result


def slider(id, maxid):
    result = InlineKeyboardMarkup()
    result.row(InlineKeyboardButton("Посмотреть покупку", callback_data="show_products"))
    result.row(
        InlineKeyboardButton("<<", callback_data=f"last~{id}"),
        InlineKeyboardButton(f"{id+1}/{maxid}", callback_data=f"pass"),
        InlineKeyboardButton(">>", callback_data=f"next~{id}"),
    )
    result.row(InlineKeyboardButton("Назад", callback_data="back_to_menu"))
    return result


back_to_menu = InlineKeyboardMarkup()
back_to_menu.row(InlineKeyboardButton("Назад", callback_data="back_to_menu"))

admin_markup = ReplyKeyboardMarkup(resize_keyboard=True)
admin_markup.row("Загрузить товар")
admin_markup.row("Выгрузить товар")
admin_markup.row("Добавить категории", "Выгрузить категорию")
admin_markup.row("Отправить сообщение пользователям")
admin_markup.row("Добавить одиночный товар")

accept_input_keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
accept_input_keyboard.row("Подтвердить")
accept_input_keyboard.row("Отмена")

cancel_markup = ReplyKeyboardMarkup(resize_keyboard=True)
cancel_markup.row("Отмена")

# append_systems = InlineKeyboardMarkup()
# append_systems.row(
#     InlineKeyboardButton("USDT", callback_data="cryptobot~USDT"),
#     InlineKeyboardButton("TON", callback_data="cryptobot~TON"),
# )
# append_systems.row(
#     InlineKeyboardButton("BTC", callback_data="cryptobot~BTC"),
#     InlineKeyboardButton("LTC", callback_data="cryptobot~LTC"),
# )
# append_systems.row(
#     InlineKeyboardButton("TRX", callback_data="cryptobot~TRX"),
# )
append_systems = InlineKeyboardMarkup()
# append_systems.row(InlineKeyboardButton("Cryptonator", callback_data="cryptonator"))
# append_systems.row(InlineKeyboardButton("Qiwi", callback_data="qiwi"))
# append_systems.row(InlineKeyboardButton("PerfectMoney", callback_data="perfectmoney"))
# append_systems.row(InlineKeyboardButton("BtcPay", callback_data="btcpay"))
# append_systems.row(InlineKeyboardButton("LtcPay", callback_data="ltcpay"))

append_systems.row(InlineKeyboardButton("PayKassa", callback_data="paykassa"))