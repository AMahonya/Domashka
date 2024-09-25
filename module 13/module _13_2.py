from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

API_TOKEN = "your api token"
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(text=["Urban"])
async def urban_message(message):
    print('Мы получили сообщение Urban!')

@dp.message_handler(commands=["start"])
async def start(massage: types.Message):
    await massage.answer("Привет! Я бот помогающий твоему здоровью.")
    print('Привет! Я бот помогающий твоему здоровью.')


@dp.message_handler(commands=["start"])
async def start_massage(message):
    print('Start massage')

@dp.message_handler()
async def help(message: types.Message):
    await message.answer('Введите команду /start, чтобы начать общение.')
    print('Введите команду /start, чтобы начать общение.')


@dp.message_handler()
async def all_massage(message):
    print('Мы получили сообщение!')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)