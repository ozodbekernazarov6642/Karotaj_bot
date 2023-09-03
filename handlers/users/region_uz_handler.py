from aiogram import types

from keyboards.inline.expedition_uz_reg import menu_expedition_uz_reg
from keyboards.inline.expedition_uz_uz import menu_expedition_uz_uz
from loader import dp
from states.uz_states import menu_uz
from utils.list import app_list


@dp.callback_query_handler(text='region_uz:"O\'zbek geologiya '
                                'qidiruv" AJ', state=menu_uz.region)
async def send_expedition(call: types.CallbackQuery):
    region = call.data.split(':')
    app_list.app_list["region"] = region[1]
    await call.message.answer("Ekspeditsiyani tanlang:", reply_markup=menu_expedition_uz_uz)
    await call.message.delete()
    await menu_uz.next()


@dp.callback_query_handler(text='region_uz:"Regionalgeologiya" DUK', state=menu_uz.region)
async def send_expedition(call: types.CallbackQuery):
    region = call.data.split(':')
    app_list.app_list["region"] = region[1]
    await call.message.delete()
    await call.message.answer("Ekspeditsiyani tanlang:", reply_markup=menu_expedition_uz_reg)
    await menu_uz.next()


@dp.callback_query_handler(text='region_uz:"Suv tarraqiyoti" MChJ', state=menu_uz.region)
async def send_expedition(call: types.callback_query):
    region = call.data.split(':')
    app_list.app_list["region"] = region[1]
    await call.answer("❌Ekspeditsiya mavjud emas", show_alert=True)


@dp.callback_query_handler(text='region_uz:"Samgeoltexservis" MChJ', state=menu_uz.region)
async def send_expedition(call: types.callback_query):
    region = call.data.split(':')
    app_list.app_list["region"] = region[1]
    await call.answer("❌Ekspeditsiya mavjud emas", show_alert=True)


@dp.callback_query_handler(text='region_uz:"Ozarbayjon" IIChB', state=menu_uz.region)
async def send_expedition(call: types.callback_query):
    region = call.data.split(':')
    app_list.app_list["region"] = region[1]
    await call.answer("❌Ekspeditsiya mavjud emas", show_alert=True)
