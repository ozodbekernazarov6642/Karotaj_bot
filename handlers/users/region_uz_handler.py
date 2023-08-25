from aiogram import types

from keyboards.inline.expedition_uz_reg import menu_expedition_uz_reg
from keyboards.inline.expedition_uz_uz import menu_expedition_uz_uz
from loader import dp
from states.lang_state import Lang_state


@dp.callback_query_handler(text="region_uz:Uz", state=Lang_state.uzb)
async def send_expedition(call: types.CallbackQuery):
    await call.message.answer("Ekspeditsiyani tanlang:", reply_markup=menu_expedition_uz_uz)
    await call.message.delete()


@dp.callback_query_handler(text="region_uz:Reg", state=Lang_state.uzb)
async def send_expedition(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Ekspeditsiyani tanlang:", reply_markup=menu_expedition_uz_reg)


@dp.callback_query_handler(text="region_uz:St", state=Lang_state.uzb)
async def send_expedition(call: types.callback_query):
    await call.answer("❌Ekspeditsiya mavjud emas", show_alert=True)


@dp.callback_query_handler(text="region_uz:Sam", state=Lang_state.uzb)
async def send_expedition(call: types.callback_query):
    await call.answer("❌Ekspeditsiya mavjud emas", show_alert=True)


@dp.callback_query_handler(text="region_uz:Oz", state=Lang_state.uzb)
async def send_expedition(call: types.callback_query):
    await call.answer("❌Ekspeditsiya mavjud emas", show_alert=True)
