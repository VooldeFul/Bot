import logging
import random
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

API_TOKEN = '6134476088:AAFOw3CxvVnPDQ7tlTIdWzF0tP9gJA80x5M'

# Инициализируем бота и диспетчер
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Включаем логирование, чтобы видеть информацию об ошибках
logging.basicConfig(level=logging.INFO)

# Список цитат
quotes = [
    "Цитата 1",
    "Цитата 2",
    "Цитата 3",
    # Добавьте свои цитаты
]

@dp.message_handler(commands=['quote'])
async def send_random_quote(message: types.Message):
    """
    Обработчик команды /quote
    """
    quote = random.choice(quotes)
    await message.reply(quote)

if __name__ == '__main__':
    # Запускаем бота
    executor.start_polling(dp, skip_updates=True)