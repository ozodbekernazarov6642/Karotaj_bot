from aiogram import types

from keyboards.inline.expedition_ru_reg import menu_expedition_ru_reg

from keyboards.inline.expedition_ru_uz import menu_expedition_ru_uz
from loader import dp
from states.uz_states import menu_uz


@dp.callback_query_handler(text="region_ru:Uz", state=menu_uz.region)
async def send_expedition(call: types.CallbackQuery):
    await call.message.answer("Выберите экспедицию:", reply_markup=menu_expedition_ru_uz)
    await call.message.delete()
    await menu_uz.next()


@dp.callback_query_handler(text="region_ru:Reg", state=menu_uz.region)
async def send_expedition(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Выберите экспедицию:", reply_markup=menu_expedition_ru_reg)
    await menu_uz.next()


@dp.callback_query_handler(text="region_ru:St", state=menu_uz.region)
async def send_expedition(call: types.callback_query):
    await call.answer("❌Экспедиция недоступна", show_alert=True)
    await menu_uz.next()


@dp.callback_query_handler(text="region_ru:Sam", state=menu_uz.region)
async def send_expedition(call: types.callback_query):
    await call.answer("❌Экспедиция недоступна", show_alert=True)
    await menu_uz.next()


@dp.callback_query_handler(text="region_ru:Oz", state=menu_uz.region)
async def send_expedition(call: types.callback_query):
    await call.answer("❌Экспедиция недоступна", show_alert=True)
    await menu_uz.next()
