from os import getenv

from dotenv import load_dotenv

load_dotenv()

TG_BOT_TOKEN = getenv("TG_BOT_TOKEN", None)

POSTGRES_DB = getenv("POSTGRES_DB", None)
POSTGRES_USER = getenv("POSTGRES_USER", None)
POSTGRES_PASSWORD = getenv("POSTGRES_PASSWORD", None)
POSTGRES_HOST = getenv("POSTGRES_HOST", None)
POSTGRES_PORT = getenv("POSTGRES_PORT", None)

BUY_URL = ["E_mir_store"]

FILE_SAVE_PATH = r"src/data/"

TEXT_HELLO_MESSAGE = [""]

TEXT_ABOUT_MESSAGE = ["Чуть позже тут появятся контактная информация"]

TEXT_HOW_BUY = [
    """Как купить:
1️⃣ Нажмите кнопку «Купить» в каталоге.
2️⃣ Напишите нашему менеджеру, что хотите приобрести.
3️⃣ Договоритесь о визите в магазин или доставке."""
]

TEXT_CONTACT_US = [
    """
    😊 Мы всегда на связи!
Задайте вопрос, уточните наличие или оформите заказ прямо в чате.
🕒 Работаем ежедневно с 11:00 до 20:00
📲 Напишите нам — ответим быстро!
    """
]

TEXT_INFO_BUTTON = [
    "Чуть позже тут появится важная информация"
]

if not all(
        (
                TG_BOT_TOKEN,
                POSTGRES_DB,
                POSTGRES_USER,
                POSTGRES_PASSWORD,
                POSTGRES_HOST,
                POSTGRES_PORT,
                BUY_URL,
                FILE_SAVE_PATH,
                TEXT_HELLO_MESSAGE,
                TEXT_ABOUT_MESSAGE,
                TEXT_HOW_BUY,
                TEXT_CONTACT_US,
        )
):
    raise Exception(
        "Not all environment variables are set. Please set them manually."
    )
