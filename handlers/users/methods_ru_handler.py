from aiogram import types
from keyboards.inline.expedition_uz_reg import menu_expedition_uz_reg
from keyboards.inline.expedition_uz_uz import menu_expedition_uz_uz
from loader import dp
from states.ru_states import menu_ru
from utils.list.app_list import app_list


@dp.callback_query_handler(text="Гамма каротаж - ГК", state=menu_ru.method)
async def send_expedition(call: types.CallbackQuery):
    app_list["method"] = call.data
    await call.message.answer("Введите время прибытия зонда (дд/мм/гггг)")
    await call.message.delete()
    await menu_ru.next()


@dp.callback_query_handler(text="'Инклинометрия - Инк", state=menu_ru.method)
async def send_expedition(call: types.CallbackQuery):
    app_list["method"] = call.data
    await call.message.answer("Введите время прибытия зонда (дд/мм/гггг)")
    await call.message.delete()
    await menu_ru.next()


@dp.callback_query_handler(text="Каротаж сопротивления - КС", state=menu_ru.method)
async def send_expedition(call: types.CallbackQuery):
    app_list["method"] = call.data
    await call.message.answer("Введите время прибытия зонда (дд/мм/гггг)")
    await call.message.delete()
    await menu_ru.next()


@dp.callback_query_handler(text="Естественный потенциал - ПС", state=menu_ru.method)
async def send_expedition(call: types.CallbackQuery):
    app_list["method"] = call.data
    await call.message.answer("Введите время прибытия зонда (дд/мм/гггг)")
    await call.message.delete()
    await menu_ru.next()


@dp.callback_query_handler(text="'Кавернометрия - КВ", state=menu_ru.method)
async def send_expedition(call: types.CallbackQuery):
    app_list["method"] = call.data
    await call.message.answer("Введите время прибытия зонда (дд/мм/гггг)")
    await call.message.delete()
    await menu_ru.next()


@dp.callback_query_handler(text="Магнитный каротаж - КМВ", state=menu_ru.method)
async def send_expedition(call: types.CallbackQuery):
    app_list["method"] = call.data
    await call.message.answer("Введите время прибытия зонда (дд/мм/гггг)")
    await call.message.delete()
    await menu_ru.next()
