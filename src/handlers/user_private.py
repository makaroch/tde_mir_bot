from aiogram import Router, F
from aiogram.filters import CommandStart, Command, ChatMemberUpdatedFilter, KICKED
from aiogram.types import Message, CallbackQuery, ChatMemberUpdated

from src.filters.chat_types import ChatTypesFilter
from src.keyboards.repl_keyboards import create_keyboard_type_product, final_keyboard, create_start_keyboard, \
    kupit_knopka, create_keyboard_product
from src.database.db_functions import DB
from src.settings import TEXT_HELLO_MESSAGE, TEXT_ABOUT_MESSAGE, TEXT_HOW_BUY, TEXT_CONTACT_US

user_private_router = Router()
user_private_router.message.filter(ChatTypesFilter(["private"]))


async def start_command_logik(message: Message):
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


@user_private_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await start_command_logik(message)


@user_private_router.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=KICKED))
async def user_blocked_bot(event: ChatMemberUpdated):
    DB.unsubscribe_user(event.chat.id)


@user_private_router.message(Command("about"))
async def echo_handler(message: Message) -> None:
    await message.answer(TEXT_ABOUT_MESSAGE[0])


@user_private_router.message(F.text == "Каталог")
async def keyboard_reaction(message: Message):
    await start_command_logik(message)


@user_private_router.message(F.text == "Контакты")
async def keyboard_reaction(message: Message):
    await message.answer(
        text=TEXT_ABOUT_MESSAGE[0],
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
        reply_markup=create_keyboard_product(int(type_id), type_name)
    )


@user_private_router.callback_query(F.data.startswith("product"))
async def echo_handler(call: CallbackQuery) -> None:
    temp_lst = call.data.split("|")
    product_id, products_type_id, product_type_name = temp_lst[1], temp_lst[2], temp_lst[3]
    await call.answer()
    await call.message.delete()
    await call.message.answer(
        text=get_str_products_by_type_id(int(product_id)),
        reply_markup=final_keyboard(products_type_id, product_type_name),
        protect_content=True
    )


def get_str_products_by_type_id(product_id: int) -> str:
    product = DB.get_product_by_id(product_id)
    return product.description
