from aiogram.types import InlineKeyboardButton, KeyboardButton
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


def create_keyboard_type_product():
    all_type_product = DB.get_all_type_product()
    keyboard = InlineKeyboardBuilder()

    if len(all_type_product) % 2 == 0:
        len_range = len(all_type_product)
    else:
        len_range = len(all_type_product) - 1

    for i in range(0, len_range, 2):
        keyboard.row(
            InlineKeyboardButton(
                text=all_type_product[i].name,
                callback_data=f"type_pr|{all_type_product[i].id}|{all_type_product[i].name}"
            ),
            InlineKeyboardButton(
                text=all_type_product[i + 1].name,
                callback_data=f"type_pr|{all_type_product[i + 1].id}|{all_type_product[i + 1].name}"
            )
        )

    if len(all_type_product) % 2 != 0:
        keyboard.row(
            InlineKeyboardButton(
                text=all_type_product[-1].name,
                callback_data=f"type_pr|{all_type_product[-1].id}|{all_type_product[-1].name}"
            )
        )

    return keyboard.as_markup()


def create_keyboard_product(products_type_id, product_type_name):
    products = DB.get_products_by_type_product(products_type_id)
    keyboard = InlineKeyboardBuilder()
    if len(products) % 2 == 0:
        len_range = len(products)
    else:
        len_range = len(products) - 1

    for i in range(0, len_range, 2):
        keyboard.row(
            InlineKeyboardButton(
                text=products[i].name,
                callback_data=f"product|{products[i].id}|{products_type_id}|{product_type_name}"  # manuf
            ),
            InlineKeyboardButton(
                text=products[i + 1].name,
                callback_data=f"product|{products[i + 1].id}|{products_type_id}|{product_type_name}"  # manuf
            )
        )

    if len(products) % 2 != 0:
        keyboard.row(
            InlineKeyboardButton(
                text=products[-1].name,
                callback_data=f"product|{products[-1].id}|{products_type_id}|{product_type_name}"  # manuf
            )
        )

    keyboard.row(
        InlineKeyboardButton(
            text='<- Назад',
            callback_data=f"main_menu"
        )
    )

    return keyboard.as_markup()


def create_keyboard_subtype(m_id, type_id, type_name):
    subtypes = DB.get_subtype_by_manufacturer_and_type_id(m_id, type_id)
    keyboard = InlineKeyboardBuilder()
    for s in subtypes:
        keyboard.row(
            InlineKeyboardButton(
                text=s.name,
                callback_data=f"subt|{s.id}|{m_id}|{type_id}|{type_name}"
            )
        )
    keyboard.row(
        InlineKeyboardButton(
            text='<- Назад',
            callback_data=f"type_pr|{type_id}|{type_name}"
        )
    )
    return keyboard.as_markup()


def final_keyboard(type_product_id, type_product_name):
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
            callback_data=f"type_pr|{type_product_id}|{type_product_name}"
        )
    )
    return keyboard.as_markup()


def kupit_knopka():
    '''нужно бооооольше провоооооооооооок'''
    keyboard = InlineKeyboardBuilder()
    keyboard.row(
        InlineKeyboardButton(
            text="написать",
            url=f"https://t.me/{BUY_URL[0]}"
        )
    )
    return keyboard.as_markup()
