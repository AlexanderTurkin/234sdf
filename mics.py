import os
import shelve

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import truverifi

from databases import User, Base
from config import token
from smsred import SmsRed


bot = Bot(token, parse_mode="html")
dp = Dispatcher(bot, storage=MemoryStorage())

engine = create_engine(f"sqlite:///base")

Base.metadata.create_all(engine)

if not os.path.isfile(f"base"):
    Base.metadata.create_all(engine)

with shelve.open("client", "c") as f:
    btcpay_client = f.get("client")
    if btcpay_client is None:
        f["client"] = btcpay_client
    ltc_client = f.get("ltc_client")
    if ltc_client is None:
        f["ltc_client"] = ltc_client
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)



# sms_red_api = SmsRed("49edeb591eb489d1fdfa4e6f7875a5ba0a506d39")

client_truverifi = truverifi.API("DjGtSdnpXaDuuI8ZAEj8AJQ0")


async def get_user_locale(state, Session, user_id):
    async with state.proxy() as f:
        loc = f.get("locale")
    if loc == None:
        session = Session()
        result = session.query(User).filter_by(id=user_id).first()
        session.close()
        return result.language
    else:
        return loc