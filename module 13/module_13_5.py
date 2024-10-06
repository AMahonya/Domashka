from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

API_TOKEN = ""
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


kb = ReplyKeyboardMarkup()
button = KeyboardButton(text="Информация")
button2 = KeyboardButton(text="Рассчитать")
kb.row(button, button2)


@dp.message_handler(commands=["start"])
async def start(massage: types.Message):
    await massage.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup=kb)


class UserStats(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text="Рассчитать")
async def set_age(massage):
    await massage.answer("Введите свой возраст: ")
    await UserStats.age.set()


@dp.message_handler(state=UserStats.age)
async def set_growth(massage, state):
    await state.update_data(age=int(massage.text))
    await state.get_data()
    await massage.answer("Введите свой рост: ")
    await UserStats.growth.set()


@dp.message_handler(state=UserStats.growth)
async def set_weight(massage, state):
    await state.update_data(growth=int(massage.text))
    await state.get_data()
    await massage.answer("Введите свой вес: ")
    await UserStats.weight.set()


@dp.message_handler(state=UserStats.weight)
async def send_calories(massage, state):
    await state.update_data(weight=int(massage.text))
    data = await state.get_data()
    calories = (10 * data["weight"]) + (6.25 * data["growth"]) - (5 * data["age"]) + 5
    await massage.answer(f"Ваша норма калорий: {calories}")
    await state.finish


@dp.message_handler(text="Информация")
async def info(message):
    await message.answer("Информация о боте:\n- Простой и удобный бот для получения информации о здоровье.")


@dp.message_handler()
async def helper(message: types.Message):
    await message.answer('Введите команду /start, чтобы начать общение.\n')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
