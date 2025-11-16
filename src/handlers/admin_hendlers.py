from aiogram import Router, F, Bot
from aiogram.filters import Command, StateFilter
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from src.filters.chat_types import ChatTypesFilter
from src.filters.is_admin import IsAdmin
from src.states.admins import AdminAddExl, AdminRefactorHelloText, AdminRefactorAboutText, AdminRefactorUsername, \
    AdminSpam, AdminHowBuyText, AdminContactUs
from src.settings import FILE_SAVE_PATH, TEXT_HELLO_MESSAGE, TEXT_ABOUT_MESSAGE, BUY_URL, TEXT_HOW_BUY, TEXT_CONTACT_US
from src.services.spam import spamming_user

admin_private_router = Router()
admin_private_router.message.filter(ChatTypesFilter(["private"]), IsAdmin())


# /load_product_from_xlsx
# /new_hello_message
# /new_about_message
# /new_manager_username


@admin_private_router.message(StateFilter(None), Command("new_hello_message"))
async def new_hello_text(message: Message, state: FSMContext):
    await message.answer("Отправьте новое приветственное сообщение!\n"
                         "Команду /empty чтобы очистить приветственное сообщение\n"
                         "Команду /cancel чтобы отменить ожидание")
    await state.set_state(AdminRefactorHelloText.start)


@admin_private_router.message(AdminRefactorHelloText.start, Command("empty"))
async def new_hello_text(message: Message, state: FSMContext):
    TEXT_HELLO_MESSAGE[0] = ""
    await message.answer("Очищено")
    await state.clear()


@admin_private_router.message(AdminRefactorHelloText.start, Command("cancel"))
async def new_hello_text(message: Message, state: FSMContext):
    await message.answer("Отменено")
    await state.clear()


@admin_private_router.message(AdminRefactorHelloText.start, F.text)
async def new_hello_text(message: Message, state: FSMContext):
    TEXT_HELLO_MESSAGE[0] = message.text
    await message.answer("Изменено")
    await state.clear()


@admin_private_router.message(AdminRefactorHelloText.start)
async def new_hello_text(message: Message, state: FSMContext):
    await message.answer("Ожидается новое приветственное сообщение\n"
                         "Отправьте новое приветственное сообщение!\n"
                         "Команду /empty чтобы очистить приветственное сообщение\n"
                         "Команду /cancel чтобы отменить ожидание")


@admin_private_router.message(StateFilter(None), Command("new_about_message"))
async def new_about_text(message: Message, state: FSMContext):
    await message.answer("Отправьте новое сообщение о нас!\n"
                         "Команду /empty чтобы очистить приветственное сообщение\n"
                         "Команду /cancel чтобы отменить ожидание")
    await state.set_state(AdminRefactorAboutText.start)


@admin_private_router.message(AdminRefactorAboutText.start, Command("empty"))
async def new_about_text(message: Message, state: FSMContext):
    TEXT_ABOUT_MESSAGE[0] = "Чуть позже тут появятся контактная информация"
    await message.answer("Очищено")
    await state.clear()


@admin_private_router.message(AdminRefactorAboutText.start, Command("cancel"))
async def new_about_text(message: Message, state: FSMContext):
    await message.answer("Отменено")
    await state.clear()


@admin_private_router.message(AdminRefactorAboutText.start, F.text)
async def new_about_text(message: Message, state: FSMContext):
    TEXT_ABOUT_MESSAGE[0] = message.text
    await message.answer("Изменено")
    await state.clear()


@admin_private_router.message(AdminRefactorAboutText.start)
async def new_about_text(message: Message, state: FSMContext):
    await message.answer("Ожидается новое сообщение о нас!\n"
                         "Отправьте новое сообщение о нас!\n"
                         "Команду /empty чтобы очистить приветственное сообщение\n"
                         "Команду /cancel чтобы отменить ожидание")


@admin_private_router.message(StateFilter(None), Command("new_manager_username"))
async def new_manager_username(message: Message, state: FSMContext):
    await message.answer("Отправьте новый username менеджера без @\n"
                         "Команду /cancel чтобы отменить ожидание")
    await state.set_state(AdminRefactorUsername.start)


@admin_private_router.message(AdminRefactorUsername.start, Command("cancel"))
async def new_manager_username(message: Message, state: FSMContext):
    await message.answer("Отменено")
    await state.clear()


@admin_private_router.message(AdminRefactorUsername.start, F.text)
async def new_manager_username(message: Message, state: FSMContext):
    BUY_URL[0] = message.text
    await message.answer("Изменено")
    await state.clear()


@admin_private_router.message(AdminRefactorUsername.start)
async def new_manager_username(message: Message, state: FSMContext):
    await message.answer("Ожидается новый username менеджера без @")


@admin_private_router.message(StateFilter(None), Command("new_newsletter"))
async def new_manager_username(message: Message, state: FSMContext):
    await message.answer("Отправь мне сообщение которое нужно разослать всем клиентам!\n"
                         "После начала рассылки её уже не отменить\n"
                         "Используй команду /cancel чтобы отменить начало рассылки")
    await state.set_state(AdminSpam.start)


@admin_private_router.message(AdminSpam.start, Command("cancel"))
async def new_manager_username(message: Message, state: FSMContext):
    await message.answer("Отменено")
    await state.clear()


@admin_private_router.message(AdminSpam.start, F.text)
async def new_manager_username(message: Message, state: FSMContext, bot: Bot):
    await message.answer("Начал рассылку...")
    await state.clear()
    await spamming_user(message_text=message.text, bot=bot)
    await message.answer("Закончил рассылку!")


@admin_private_router.message(AdminSpam.start)
async def new_manager_username(message: Message):
    await message.answer("Ожидается ТЕКСТ сообщения для рассылки\n"
                         "Используй команду /cancel чтобы отменить начало рассылки")


@admin_private_router.message(StateFilter(None), Command("new_how_buy_text"))
async def new_manager_username(message: Message, state: FSMContext):
    await message.answer("Отправь мне текст нового сообщения для кнопки 'Как купить'\n"
                         "Используй команду /cancel чтобы отменить ожидание")
    await state.set_state(AdminHowBuyText.start)


@admin_private_router.message(AdminHowBuyText.start, Command("cancel"))
async def new_manager_username(message: Message, state: FSMContext):
    await message.answer("Отменено")
    await state.clear()


@admin_private_router.message(AdminHowBuyText.start, F.text)
async def new_manager_username(message: Message, state: FSMContext, bot: Bot):
    await state.clear()
    TEXT_HOW_BUY[0] = message.text
    await message.answer("Изменено")


@admin_private_router.message(AdminHowBuyText.start)
async def new_manager_username(message: Message):
    await message.answer("Ожидается ТЕКСТ сообщения кнопки 'Как купить'\n"
                         "Используй команду /cancel чтобы отменить ожидание")


@admin_private_router.message(StateFilter(None), Command("new_contact_text"))
async def new_manager_username(message: Message, state: FSMContext):
    await message.answer("Отправь мне текст нового сообщения для кнопки 'Связаться с нами'\n"
                         "Используй команду /cancel чтобы отменить ожидание")
    await state.set_state(AdminContactUs.start)


@admin_private_router.message(AdminContactUs.start, Command("cancel"))
async def new_manager_username(message: Message, state: FSMContext):
    await message.answer("Отменено")
    await state.clear()


@admin_private_router.message(AdminContactUs.start, F.text)
async def new_manager_username(message: Message, state: FSMContext, bot: Bot):
    await state.clear()
    TEXT_CONTACT_US[0] = message.text
    await message.answer("Изменено")


@admin_private_router.message(AdminContactUs.start)
async def new_manager_username(message: Message):
    await message.answer("Ожидается ТЕКСТ сообщения кнопки 'Связаться с нами'\n"
                         "Используй команду /cancel чтобы отменить ожидание")
