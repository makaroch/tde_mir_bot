import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import BotCommandScopeAllPrivateChats

from src.settings import TG_BOT_TOKEN
from src.handlers.routers import handlers_router
from src.command.bot_command import private_command

dp = Dispatcher()


async def main():
    bot = Bot(token=TG_BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    bot.my_admins_lst = []
    dp.include_router(handlers_router)
    await bot.set_my_commands(commands=private_command, scope=BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
