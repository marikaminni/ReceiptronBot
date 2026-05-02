import os
import dotenv
from dotenv import load_dotenv

#carica chiave api e gestione exception find_dotenv()
env_path = dotenv.find_dotenv(".env")
if not env_path:
    raise FileNotFoundError(".env not found")

load_dotenv(env_path)
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
if not BOT_TOKEN:
    raise ValueError('BOT_TOKEN must be set')

GEMINI_KEY = os.getenv('GEMINI_API_KEY')
if not GEMINI_KEY:
    raise ValueError('GEMINI_KEY must be set')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(BASE_DIR, 'app', 'images', 'temp')
DB_PATH = os.path.join(BASE_DIR, "app","db",'receipt.db')