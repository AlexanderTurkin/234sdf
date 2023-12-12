from sqlalchemy import Column, Integer, String, Text, Float, DateTime, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=True)
    language = Column(Text)
    balance = Column(Integer, default=0)


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, autoincrement=True)
    file_id = Column(Text, nullable=True)
    text = Column(Text)
    product_type = Column(Integer)
    is_sold = Column(Boolean, default=False)
    sold_datetime = Column(DateTime, nullable=True)
    sold_id = Column(Integer, nullable=True)


class SingleProduct(Base):
    __tablename__ = "single_products"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text)
    text = Column(Text)
    price = Column(Float)
    is_sold = Column(Boolean, default=False)
    sold_datetime = Column(DateTime, nullable=True)
    sold_id = Column(Integer, nullable=True)
    type = Column(Text)


# class Accounts(Base):
#     __tablename__ = "single_products"
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(Text)
#     text = Column(Text)
#     price = Column(Float)
#     is_sold = Column(Boolean, default=False)
#     sold_datetime = Column(DateTime, nullable=True)
#     sold_id = Column(Integer, nullable=True)


class QiwiTransactions(Base):
    __tablename__ = "qiwi_transactions"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer)
    sum = Column(Float)
    bill_id = Column(Integer)
    status = Column(Boolean, default=False)


class PMTransactions(Base):
    __tablename__ = "pm_transactions"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer)
    sum = Column(Float)
    bill_id = Column(Integer)
    status = Column(Boolean, default=False)


class CryptoBotTransactions(Base):
    __tablename__ = "crypto_bot_transactions"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer)
    currency = Column(Text)
    sum = Column(Float)
    bill_id = Column(Integer)
    status = Column(Boolean, default=False)


class Categories(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Text)
    count = Column(Integer)
    price = Column(Float)


class Sold(Base):
    __tablename__ = "sold"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    sold_date = Column(DateTime)


class Transactions(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer)
    url = Column(Text)
    invoice_id = Column(Text)
    status = Column(Text, default="unpaid")