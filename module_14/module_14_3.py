import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio
from API import *

logging.basicConfig(level=logging.INFO,
                    filemode="w",
                    filename="loging_TG_BOT.log",
                    encoding= 'utf-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')


bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


start_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
start_button = KeyboardButton("Начать")
start_kb.add(start_button)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text="Информация")
button2 = KeyboardButton(text="Рассчитать")
button3 = KeyboardButton(text="Купить")
kb.row(button, button2)
kb.add(button3)

in_kb = InlineKeyboardMarkup(resize_keyboard=True)
in_button = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data="calories")
in_button1 = InlineKeyboardButton(text="Формулы расчёта", callback_data="formulas")
in_kb.add(in_button, in_button1)


in_kb2 = InlineKeyboardMarkup(resize_keyboard=True)
in_button2 = InlineKeyboardButton(text = "Amino Isolate", callback_data="product_buying")
in_button3 = InlineKeyboardButton(text = "Amino Tabs", callback_data="product_buying")
in_button4 = InlineKeyboardButton(text = "Mega Massa", callback_data="product_buying")
in_button5 = InlineKeyboardButton(text = "Whey Protein", callback_data="product_buying")
in_kb2.add(in_button2, in_button3, in_button4, in_button5)


class UserStats(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text=["Начать"])
async def start(message: types.Message):
    await message.answer(
        "Привет! 👋 \n"
        "Я бот помогающий твоему здоровью. 🦠👩‍⚕🧬🩺💉  \n",
        reply_markup=kb
    )


@dp.message_handler(text=["Рассчитать"])
async def main_menu(message):
    await message.answer(
        "Выберите опцию:' \n",
        reply_markup=in_kb
    )


@dp.callback_query_handler(text="formulas")
async def formulas(call):
    await call.message.answer(
        "Формулы расчёта:\n"
        "1. Норма калорий = (10 * вес) + (6.25 * рост) - (5 * возраст) + 5\n"
        "2. При высокой активности = норма калорий * 1.25\n"
    )


@dp.callback_query_handler(text="calories")
async def set_age(call):
    await call.message.answer("Введите свой возраст: ")
    await UserStats.age.set()


@dp.message_handler(state=UserStats.age)
async def set_growth(message, state):
    await state.update_data(age=int(message.text))
    await state.get_data()
    await message.answer("Введите свой рост: ")
    await UserStats.growth.set()


@dp.message_handler(state=UserStats.growth)
async def set_weight(message, state):
    await state.update_data(growth=int(message.text))
    await state.get_data()
    await message.answer("Введите свой вес: ")
    await UserStats.weight.set()


@dp.message_handler(state=UserStats.weight)
async def send_calories(message, state):
    await state.update_data(weight=int(message.text))
    data = await state.get_data()
    calories = (10 * data["weight"]) + (6.25 * data["growth"]) - (5 * data["age"]) + 5
    await message.answer(f"Ваша норма калорий: {calories}")
    await state.finish()


@dp.message_handler(text="Информация")
async def info(message):
    await message.answer("Информация о боте:\n- Простой и удобный бот для получения информации о здоровье.")


@dp.message_handler(text="Купить")
async def get_buying_list(message):
    with open("fail\Amino_Isolate.jpg", "rb") as photo:
        await message.answer_photo(photo,
                                   "Название: Amino Isolate | Описание: 280 гр | Цена: 1990 ₽\n")

    with open("fail\Amino_Tabs.jpg", "rb") as photo:
        await message.answer_photo(photo,
                                   "Название: Amino Tabs | Описание: 200 таблеток | Цена: 3200 ₽\n")

    with open("fail\Mega_Massa.jpg", "rb") as photo:
        await message.answer_photo(photo,
                                   "Название: Mega Mass | Описание: 3000 гр | Цена: 8229 ₽\n")

    with open("fail\Whey_protein.jpg", "rb") as photo:
        await message.answer_photo(photo,
                                    "Название: Whey Protein | Описание: 1000 гр | Цена: 6555 ₽\n")

    await message.answer(
        "Выберите продукт для покупки:' \n",
        reply_markup=in_kb2
    )

@dp.callback_query_handler(text="product_buying")
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer("")




@dp.message_handler()
async def helper(message: types.Message):
    await message.answer("👋", reply_markup=start_kb)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
