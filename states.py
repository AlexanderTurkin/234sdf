from aiogram.utils.helper import Helper, HelperMode, ListItem
from aiogram.dispatcher.filters.state import State, StatesGroup

class Form(StatesGroup):
    AwaitCount = State()
    AwaitSumForAppend = State()

class Admin(StatesGroup):
    AwaitCategory = State()
    AwaitOutput = State()
    AwaitMassCategory = State()
    AwaitOutputCategory = State()
    AwaitSingleProductContent = State()
    AwaitSingleProduct = State()