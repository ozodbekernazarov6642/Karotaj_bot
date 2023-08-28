from aiogram import types

from keyboards.inline.plot_ru_reg import menu_plot_ru_muz, menu_plot_ru_qor
from keyboards.inline.plot_ru_uz import menu_plot_ru_zarafshon, menu_plot_ru_shim, menu_plot_ru_zarmitan, \
    menu_plot_ru_hisor, menu_plot_ru_surxon, menu_plot_ru_kuk
from loader import dp
from states.uz_states import menu_uz


@dp.callback_query_handler(text="expedition_ru:Zarafshon", state=menu_uz.expedition)
async def send_expedition(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Выберите участок:", reply_markup=menu_plot_ru_zarafshon)
    await menu_uz.next()


@dp.callback_query_handler(text="expedition_ru:Shim", state=menu_uz.expedition)
async def send_expedition(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Выберите участок:", reply_markup=menu_plot_ru_shim)
    await menu_uz.next()


@dp.callback_query_handler(text="expedition_ru:Zarmitan", state=menu_uz.expedition)
async def send_expedition(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Выберите участок:", reply_markup=menu_plot_ru_zarmitan)
    await menu_uz.next()


@dp.callback_query_handler(text="expedition_ru:Hisor", state=menu_uz.expedition)
async def send_expedition(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Выберите участок:", reply_markup=menu_plot_ru_hisor)
    await menu_uz.next()


@dp.callback_query_handler(text="expedition_ru:Surxon", state=menu_uz.expedition)
async def send_expedition(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Выберите участок:", reply_markup=menu_plot_ru_surxon)
    await menu_uz.next()


@dp.callback_query_handler(text="expedition_ru:Kuk", state=menu_uz.expedition)
async def send_expedition(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Выберите участок:", reply_markup=menu_plot_ru_kuk)
    await menu_uz.next()


@dp.callback_query_handler(text="expedition_ru:Da", state=menu_uz.expedition)
async def send_expedition(call: types.callback_query):
    await call.answer("❌Участок недоступен", show_alert=True)
    await menu_uz.next()


@dp.callback_query_handler(text="expedition_ru:Muz", state=menu_uz.expedition)
async def send_expedition(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Выберите участок:", reply_markup=menu_plot_ru_muz)
    await menu_uz.next()


@dp.callback_query_handler(text="expedition_ru:Qor", state=menu_uz.expedition)
async def send_expedition(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Выберите участок:", reply_markup=menu_plot_ru_qor)
    await menu_uz.next()


@dp.callback_query_handler(text="expedition_ru:Shar", state=menu_uz.expedition)
async def send_expedition(call: types.callback_query):
    await call.answer("❌Участок недоступен", show_alert=True)
    await menu_uz.next()


@dp.callback_query_handler(text="expedition_ru:Mar", state=menu_uz.expedition)
async def send_expedition(call: types.callback_query):
    await call.answer("❌Участок недоступен", show_alert=True)
    await menu_uz.next()
