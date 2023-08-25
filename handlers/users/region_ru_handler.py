from aiogram import types

from keyboards.inline.expedition_ru_reg import menu_expedition_ru_reg

from keyboards.inline.expedition_ru_uz import menu_expedition_ru_uz
from loader import dp
from states.lang_state import Lang_state


@dp.callback_query_handler(text="region_ru:Uz", state=Lang_state.ru)
async def send_expedition(call: types.CallbackQuery):
    await call.message.answer("Выберите экспедицию:", reply_markup=menu_expedition_ru_uz)
    await call.message.delete()


@dp.callback_query_handler(text="region_ru:Reg", state=Lang_state.ru)
async def send_expedition(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Выберите экспедицию:", reply_markup=menu_expedition_ru_reg)


@dp.callback_query_handler(text="region_ru:St", state=Lang_state.ru)
async def send_expedition(call: types.callback_query):
    await call.answer("❌Экспедиция недоступна", show_alert=True)


@dp.callback_query_handler(text="region_ru:Sam", state=Lang_state.ru)
async def send_expedition(call: types.callback_query):
    await call.answer("❌Экспедиция недоступна", show_alert=True)


@dp.callback_query_handler(text="region_ru:Oz", state=Lang_state.ru)
async def send_expedition(call: types.callback_query):
    await call.answer("❌Экспедиция недоступна", show_alert=True)
