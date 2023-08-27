from aiogram import types

from keyboards.inline.expedition_uz_reg import menu_expedition_uz_reg
from keyboards.inline.expedition_uz_uz import menu_expedition_uz_uz
from loader import dp
from states.uz_states import menu_uz


@dp.callback_query_handler(text="region_uz:Uz", state=menu_uz.uz_lang)
async def send_expedition(call: types.CallbackQuery):
    await call.message.answer("Ekspeditsiyani tanlang:", reply_markup=menu_expedition_uz_uz)
    await call.message.delete()
    await menu_uz.next()


@dp.callback_query_handler(text="region_uz:Reg", state=menu_uz.region)
async def send_expedition(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Ekspeditsiyani tanlang:", reply_markup=menu_expedition_uz_reg)
    await menu_uz.next()


@dp.callback_query_handler(text="region_uz:St", state=menu_uz.region)
async def send_expedition(call: types.callback_query):
    await call.answer("❌Ekspeditsiya mavjud emas", show_alert=True)
    await menu_uz.next()


@dp.callback_query_handler(text="region_uz:Sam", state=menu_uz.region)
async def send_expedition(call: types.callback_query):
    await call.answer("❌Ekspeditsiya mavjud emas", show_alert=True)
    await menu_uz.next()


@dp.callback_query_handler(text="region_uz:Oz", state=menu_uz.region)
async def send_expedition(call: types.callback_query):
    await call.answer("❌Ekspeditsiya mavjud emas", show_alert=True)
    await menu_uz.next()
