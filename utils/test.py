import os
from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio
import logging
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, executor
from aiogram.types import BotCommand
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from constants import VEHICLES, PERIODS

# from app.config_reader import load_config
# from app.handlers.drinks import register_handlers_drinks
# from app.handlers.food import register_handlers_food
# from app.handlers.common import register_handlers_common

logger = logging.getLogger(__name__)

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/drinks", description="Заказать напитки"),
        BotCommand(command="/food", description="Заказать блюда"),
        BotCommand(command="/cancel", description="Отменить текущее действие")
    ]
    await bot.set_my_commands(commands)


async def main():
    # Настройка логирования в stdout
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )
    logger.error("Starting bot")

    # Парсинг файла конфигурации
    # config = load_config("config/bot.ini")

# Объявление и инициализация объектов бота и диспетчера
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


available_drinks_names = VEHICLES
available_drinks_sizes = PERIODS


class OrderDrinks(StatesGroup):
    waiting_for_drink_name = State()
    waiting_for_drink_size = State()



# @dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer(
        "Выберите, что хотите заказать: напитки (/drinks) или блюда (/food).",
        reply_markup=types.ReplyKeyboardRemove()
    )


@dp.message_handler(commands=['test'])
async def drinks_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for name in available_drinks_names:
        keyboard.add(name)
    await message.answer('Привет, выбери технику', reply_markup=keyboard)
    await OrderDrinks.waiting_for_drink_name.set()


async def drinks_chosen(message: types.Message, state: FSMContext):
    if message.text not in available_drinks_names:
        await message.answer("Пожалуйста, выбери технику, используя клавиатуру ниже.")
        return
    await state.update_data(chosen_food=message.text.lower())

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for size in available_drinks_sizes:
        keyboard.add(size)
    # для простых шагов можно не указывать название состояния, обходясь next()
    await OrderDrinks.next()
    await message.answer("Теперь выбери необходимый период времени", reply_markup=keyboard)


async def drinks_size_chosen(message: types.Message, state: FSMContext):
    if message.text not in available_drinks_sizes:
        await message.answer("Пожалуйста, выбери период, используя клавиатуру ниже.")
        return
    user_data = await state.get_data()
    await message.answer(f"Вы выбрали {user_data['chosen_food']} на следующий период: {message.text.lower()}.\n",
                         reply_markup=types.ReplyKeyboardRemove())
    await state.finish()


def register_handlers_drinks(dp: Dispatcher):
    dp.register_message_handler(drinks_start, commands="drinks", state="*")
    dp.register_message_handler(drinks_chosen, state=OrderDrinks.waiting_for_drink_name)
    dp.register_message_handler(drinks_size_chosen, state=OrderDrinks.waiting_for_drink_size)


# await set_commands(bot)

if __name__ == '__main__':
    register_handlers_drinks(dp)
    executor.start_polling(dp, skip_updates=True)
