import os

from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')  # тестовый чат
ADMIN_TELEGRAM_ID = os.getenv('ADMIN_TELEGRAM_ID')
PASSWORD = os.getenv('PASSWORD')
MESSAGE_THREAD_ID = os.getenv('MESSAGE_THREAD_ID')
