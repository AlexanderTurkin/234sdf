import asyncio
from aiogram.utils import executor
from mics import dp

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    executor.start_polling(dp, loop=loop)
