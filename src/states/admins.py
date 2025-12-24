from aiogram.fsm.state import State, StatesGroup


class AdminAddExl(StatesGroup):
    start = State()


class AdminRefactorHelloText(StatesGroup):
    start = State()


class AdminRefactorAboutText(StatesGroup):
    start = State()


class AdminRefactorUsername(StatesGroup):
    start = State()


class AdminSpam(StatesGroup):
    start = State()


class AdminHowBuyText(StatesGroup):
    start = State()


class AdminContactUs(StatesGroup):
    start = State()


class AdminInfoBtn(StatesGroup):
    start = State()
