from aiogram.types import InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

from src.database.db_functions import DB
from src.settings import BUY_URL


def create_start_keyboard():
    m = ReplyKeyboardBuilder()
    m.row(
        KeyboardButton(text="Как купить"),
        KeyboardButton(text="Связаться с нами"),
    )
    return m.as_markup(resize_keyboard=True)


def create_keyboard_manufacturer(products_type_id, products_type_name):
    manufacturer = DB.get_manufacturer_by_type_product(products_type_id)

    keyboard = InlineKeyboardBuilder()
    for m in manufacturer:
        keyboard.row(
            InlineKeyboardButton(
                text=m.name,
                callback_data=f"manufacturer_{m.id}_{m.name}_{products_type_id}_{products_type_name}"
            )
        )
    keyboard.row(
        InlineKeyboardButton(
            text='<- Назад',
            callback_data=f"main_menu"
        )
    )

    return keyboard.as_markup()


def create_keyboard_type_product():
    all_type_product = DB.get_all_type_product()

    keyboard = InlineKeyboardBuilder()
    for type_product in all_type_product:
        keyboard.row(
            InlineKeyboardButton(
                text=type_product.name,
                callback_data=f"type_product_{type_product.id}_{type_product.name}"
            )
        )

    return keyboard.as_markup()


def create_keyboard_subtype(m_id, m_name, type_id, type_name):
    subtypes = DB.get_subtype_by_manufacturer_and_type_id(m_id, type_id)
    keyboard = InlineKeyboardBuilder()
    for s in subtypes:
        keyboard.row(
            InlineKeyboardButton(
                text=s.name,
                callback_data=f"subtypes_{s.id}_{s.name}_{m_id}_{m_name}_{type_id}_{type_name}"
            )
        )
    keyboard.row(
        InlineKeyboardButton(
            text='<- Назад',
            callback_data=f"type_product_{type_id}_{type_name}"
        )
    )
    return keyboard.as_markup()


def final_keyboard(m_id, m_name, products_type_id, products_type_name, ):
    keyboard = InlineKeyboardBuilder()
    keyboard.row(
        InlineKeyboardButton(
            text="Купить",
            url=f"https://t.me/{BUY_URL[0]}"
        )
    )
    keyboard.row(
        InlineKeyboardButton(
            text='<- Назад',
            callback_data=f"manufacturer_{m_id}_{m_name}_{products_type_id}_{products_type_name}"
        )
    )
    return keyboard.as_markup()


def kupit_knopka():
    '''нужно бооооольше провоооооооооооок'''
    keyboard = InlineKeyboardBuilder()
    keyboard.row(
        InlineKeyboardButton(
            text="❓задать вопрос",
            url=f"https://t.me/{BUY_URL[0]}"
        )
    )
    return keyboard.as_markup()
