from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from keyboards.default.lang_uz_button import menu_send_button_uz
from keyboards.inline.expedition_uz_inlineKeyboard import menu_expedition_uz_uz, menu_expedition_uz_reg
from keyboards.inline.plot_uz_inlineKeyboard import menu_plot_uz_zarafshon, menu_plot_uz_shim
from states.lang_state import Lang_state
from keyboards.inline.region_uz_InlineKeyboard import menu_region_uz

from loader import dp, bot


@dp.message_handler(text="🇺🇿 O'zbekcha")
async def table_uz(message: types.Message):
    await message.answer("Tugmalardan birini tanlang🤳", reply_markup=menu_send_button_uz)
    await Lang_state.uzb.set()


@dp.message_handler(text="✍🏻 Buyurtma berish", state=Lang_state.uzb)
async def send_application(message: types.Message):
    await message.answer("Buyurtma Hududni tanlang", reply_markup=menu_region_uz)


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


@dp.callback_query_handler(text="expedition_uz:Zarafshon", state=Lang_state.uzb)
async def send_expedition(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Uchastkani tanlang:", reply_markup=menu_plot_uz_zarafshon)


@dp.callback_query_handler(text="expedition_uz:Shim", state=Lang_state.uzb)
async def send_expedition(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Uchastkani tanlang:", reply_markup=menu_plot_uz_shim)
