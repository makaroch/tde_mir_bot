from os import getenv

from dotenv import load_dotenv

load_dotenv()

TG_BOT_TOKEN = getenv("TG_BOT_TOKEN")

POSTGRES_DB = getenv("POSTGRES_DB")
POSTGRES_USER = getenv("POSTGRES_USER")
POSTGRES_PASSWORD = getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = getenv("POSTGRES_HOST")
POSTGRES_PORT = getenv("POSTGRES_PORT")

BUY_URL = ["E_mir_store"]

FILE_SAVE_PATH = r"src/data/"

TEXT_HELLO_MESSAGE = [""]

TEXT_ABOUT_MESSAGE = ["Чуть позже тут появятся контактная информация"]
