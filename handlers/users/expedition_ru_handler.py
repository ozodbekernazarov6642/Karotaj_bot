from aiogram import types

from keyboards.inline.plot_ru_reg import menu_plot_ru_muz, menu_plot_ru_qor
from keyboards.inline.plot_ru_uz import menu_plot_ru_zarafshon, menu_plot_ru_shim, menu_plot_ru_zarmitan, \
    menu_plot_ru_hisor, menu_plot_ru_surxon, menu_plot_ru_kuk
from loader import dp
from states.lang_state import Lang_state


@dp.callback_query_handler(text="expedition_ru:Zarafshon", state=Lang_state.ru)
async def send_expedition(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Выберите участок:", reply_markup=menu_plot_ru_zarafshon)


@dp.callback_query_handler(text="expedition_ru:Shim", state=Lang_state.ru)
async def send_expedition(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Выберите участок:", reply_markup=menu_plot_ru_shim)


@dp.callback_query_handler(text="expedition_ru:Zarmitan", state=Lang_state.ru)
async def send_expedition(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Выберите участок:", reply_markup=menu_plot_ru_zarmitan)


@dp.callback_query_handler(text="expedition_ru:Hisor", state=Lang_state.ru)
async def send_expedition(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Выберите участок:", reply_markup=menu_plot_ru_hisor)


@dp.callback_query_handler(text="expedition_ru:Surxon", state=Lang_state.ru)
async def send_expedition(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Выберите участок:", reply_markup=menu_plot_ru_surxon)


@dp.callback_query_handler(text="expedition_ru:Kuk", state=Lang_state.ru)
async def send_expedition(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Выберите участок:", reply_markup=menu_plot_ru_kuk)


@dp.callback_query_handler(text="expedition_ru:Da", state=Lang_state.ru)
async def send_expedition(call: types.callback_query):
    await call.answer("❌Участок недоступен", show_alert=True)


@dp.callback_query_handler(text="expedition_ru:Muz", state=Lang_state.ru)
async def send_expedition(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Выберите участок:", reply_markup=menu_plot_ru_muz)


@dp.callback_query_handler(text="expedition_ru:Qor", state=Lang_state.ru)
async def send_expedition(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Выберите участок:", reply_markup=menu_plot_ru_qor)


@dp.callback_query_handler(text="expedition_ru:Shar", state=Lang_state.ru)
async def send_expedition(call: types.callback_query):
    await call.answer("❌Участок недоступен", show_alert=True)


@dp.callback_query_handler(text="expedition_ru:Mar", state=Lang_state.ru)
async def send_expedition(call: types.callback_query):
    await call.answer("❌Участок недоступен", show_alert=True)
