from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

API_TOKEN = "7219838987:AAF2m50EIvxU9KWzOHslZHzIiniP0yh2FQE"
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(commands=["start"])
async def start(massage: types.Message):
    await massage.answer("Привет! Я бот помогающий твоему здоровью.")


class UserStats(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text=["Calories"])
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


@dp.message_handler()
async def helper(message: types.Message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
