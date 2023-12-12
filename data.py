import shelve
from databases import User
from mics import Session

"""
with shelve.open('Products','c') as Products:
    Products['Анимашки'] = {}
#    Products['Смайлики'] = {'test': Product(20,1),'test2':Product(20,1)}

with shelve.open('Admins','c') as Admins:
    Admins['categs_price'] = {}
"""
import sqlite3
import datetime
import random
import os.path
from collections import Counter

class Database:

	def __init__(self):

		BASE_DIR = os.path.dirname(os.path.abspath(__file__))
		db_path = os.path.join(BASE_DIR, "mysql.db")

		self.connection = sqlite3.connect(db_path)
		self.cursor = self.connection.cursor()


	def get_username(self):

		""" Получение значения имени """

		with self.connection:

			rows = self.cursor.execute('SELECT * FROM `users`').fetchall()
			return rows

db = Database()
user_ls = db.get_username()
print(user_ls)
session = Session()
for i in user_ls:
    print(i)
    newItem = User(id = i[0],name = i[1],language='ru',balance = i[2])
    session.add(newItem)
    try:
        session.commit()
    except:
        session.rollback()
session.close()