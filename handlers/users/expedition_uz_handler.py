from aiogram import types

from keyboards.inline.plot_uz_reg import menu_plot_uz_muz
from keyboards.inline.plot_uz_uz import menu_plot_uz_zarafshon, menu_plot_uz_shim, menu_plot_uz_zarmitan, \
    menu_plot_uz_hisor, menu_plot_uz_surxon, menu_plot_uz_kuk
from loader import dp
from states.lang_state import Lang_state


@dp.callback_query_handler(text="expedition_uz:Zarafshon", state=Lang_state.uzb)
async def send_expedition(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Uchastkani tanlang:", reply_markup=menu_plot_uz_zarafshon)


@dp.callback_query_handler(text="expedition_uz:Shim", state=Lang_state.uzb)
async def send_expedition(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Uchastkani tanlang:", reply_markup=menu_plot_uz_shim)


@dp.callback_query_handler(text="expedition_uz:Zarmitan", state=Lang_state.uzb)
async def send_expedition(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Uchastkani tanlang:", reply_markup=menu_plot_uz_zarmitan)


@dp.callback_query_handler(text="expedition_uz:Hisor", state=Lang_state.uzb)
async def send_expedition(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Uchastkani tanlang:", reply_markup=menu_plot_uz_hisor)


@dp.callback_query_handler(text="expedition_uz:Surxon", state=Lang_state.uzb)
async def send_expedition(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Uchastkani tanlang:", reply_markup=menu_plot_uz_surxon)


@dp.callback_query_handler(text="expedition_uz:Kuk", state=Lang_state.uzb)
async def send_expedition(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Uchastkani tanlang:", reply_markup=menu_plot_uz_kuk)


@dp.callback_query_handler(text="expedition_uz:Da", state=Lang_state.uzb)
async def send_expedition(call: types.callback_query):
    await call.answer("❌Uchastka mavjud emas", show_alert=True)


@dp.callback_query_handler(text="expedition_uz:Muz", state=Lang_state.uzb)
async def send_expedition(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Uchastkani tanlang:", reply_markup=menu_plot_uz_muz)
