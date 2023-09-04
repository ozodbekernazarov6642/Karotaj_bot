from aiogram import types

from keyboards.inline.expedition_ru_reg import menu_expedition_ru_reg
from keyboards.inline.expedition_ru_uz import menu_expedition_ru_uz
from loader import dp
from states.ru_states import menu_ru
from states.uz_states import menu_uz
from utils.list import app_list


@dp.callback_query_handler(text='region_ru:АО "Ўзбек геология қидирув"', state=menu_ru.region)
async def send_expedition(call: types.CallbackQuery):
    region = call.data.split(':')
    app_list.app_list["region"] = region[1]
    await call.message.answer("Выберите экспедицию:", reply_markup=menu_expedition_ru_uz)
    await call.message.delete()
    await menu_ru.next()


@dp.callback_query_handler(text='region_ru:"Регионалгеология" ДМ', state=menu_ru.region)
async def send_expedition(call: types.CallbackQuery):
    region = call.data.split(':')
    app_list.app_list["region"] = region[1]
    await call.message.delete()
    await call.message.answer("Выберите экспедицию:", reply_markup=menu_expedition_ru_reg)
    await menu_ru.next()


@dp.callback_query_handler(text='region_ru:СП "Сув тараққиёти"', state=menu_ru.region)
async def send_expedition(call: types.callback_query):
    region = call.data.split(':')
    app_list.app_list["region"] = region[1]
    await call.answer("❌Экспедиция недоступна", show_alert=True)


@dp.callback_query_handler(text='region_ru:ООО "Самгеолтехсервис"', state=menu_ru.region)
async def send_expedition(call: types.callback_query):
    region = call.data.split(':')
    app_list.app_list["region"] = region[1]
    await call.answer("❌Экспедиция недоступна", show_alert=True)


@dp.callback_query_handler(text='region_ru:НПО "Азербайджан"', state=menu_ru.region)
async def send_expedition(call: types.callback_query):
    region = call.data.split(':')
    app_list.app_list["region"] = region[1]
    await call.answer("❌Экспедиция недоступна", show_alert=True)
