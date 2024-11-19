from aiogram import Router, F
from aiogram.filters import CommandStart, Command, ChatMemberUpdatedFilter, KICKED
from aiogram.types import Message, CallbackQuery, ChatMemberUpdated

from src.filters.chat_types import ChatTypesFilter
from src.keyboards.repl_keyboards import create_keyboard_type_product, create_keyboard_manufacturer, \
    create_keyboard_subtype, final_keyboard, create_start_keyboard, kupit_knopka
from src.database.db_functions import DB
from src.settings import TEXT_HELLO_MESSAGE, TEXT_ABOUT_MESSAGE

user_private_router = Router()
user_private_router.message.filter(ChatTypesFilter(["private"]))


@user_private_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    DB.create_new_user_if_not_exists(
        tg_user_id=message.from_user.id,
        username=str(message.from_user.username),
    )

    await message.answer(
        text=f"Здравствуйте{', ' + message.from_user.first_name if message.from_user.first_name else ''}!\n"
             f"{'\n' + TEXT_HELLO_MESSAGE[0] + '\n' if TEXT_HELLO_MESSAGE[0] else ''}\n",
        reply_markup=create_start_keyboard()
    )
    await message.answer(
        text=f"Выберите категорию: ",
        reply_markup=create_keyboard_type_product()
    )


@user_private_router.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=KICKED))
async def user_blocked_bot(event: ChatMemberUpdated):
    DB.unsubscribe_user(event.chat.id)


@user_private_router.message(Command("about"))
async def echo_handler(message: Message) -> None:
    await message.answer(TEXT_ABOUT_MESSAGE[0])


@user_private_router.message(F.text == "Как купить")
async def keyboard_reaction(message: Message):
    await message.answer(
"""Чтобы осуществить покупку: 

1. Нажмите в каталоге кнопку «Купить». 
2. Напишите нашему менеджеру в чат, что хотите приобрести.
3. Договоритесь о визите в магазин или доставке.

Доставка по Москве осуществляется БЕСПЛАТНО! 

✅У нас только оригинальная продукция. 
✅Любые проверки перед покупкой. 
✅Trade-in ваших старых девайсов.""")


@user_private_router.message(F.text == "Связаться с нами")
async def keyboard_reaction(message: Message):
    await message.answer(
        text="Напишите менеджеру",
        reply_markup=kupit_knopka()
    )


@user_private_router.callback_query(F.data.startswith("main_menu"))
async def echo_handler(call: CallbackQuery) -> None:
    await call.message.delete()
    await call.message.answer(
        text=f"Выберите категорию: ",
        reply_markup=create_keyboard_type_product()
    )


@user_private_router.callback_query(F.data.startswith("type_pr"))
async def echo_handler(call: CallbackQuery) -> None:
    temp_lst = call.data.split("|")
    type_id, type_name = temp_lst[1], temp_lst[2]
    await call.answer()
    await call.message.delete()
    await call.message.answer(
        text=f"Категория <b>{type_name}</b>",
        reply_markup=create_keyboard_manufacturer(type_id, type_name)
    )


@user_private_router.callback_query(F.data.startswith("manuf"))
async def echo_handler(call: CallbackQuery) -> None:
    temp_lst = call.data.split("|")
    m_id, type_id, type_name = temp_lst[1], temp_lst[2], temp_lst[3]
    await call.answer()
    await call.message.delete()
    await call.message.answer(
        text=f"Категория <b>{type_name}</b>\n",
        reply_markup=create_keyboard_subtype(m_id, type_id, type_name)
    )


@user_private_router.callback_query(F.data.startswith("subt"))
async def echo_handler(call: CallbackQuery) -> None:
    temp_lst = call.data.split("|")
    subtypes_id, m_id, type_id, type_name = temp_lst[1], temp_lst[2], temp_lst[3], temp_lst[4]
    await call.answer()
    await call.message.delete()
    await call.message.answer(
        text=f"Категория <b>{type_name}</b>\n"
             f"{get_str_all_product_by_subtypes_id(int(subtypes_id))}",
        reply_markup=final_keyboard(m_id, type_id, type_name)
    )


def get_str_all_product_by_subtypes_id(subtypes_id: int) -> str:
    products = DB.get_all_product_by_subtypes_id(subtypes_id)
    result = ""
    for product in products:
        result += f"* {product.name} - {product.price}\n\n"
    return result
