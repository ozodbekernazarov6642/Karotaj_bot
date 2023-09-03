from aiogram import types
from aiogram.dispatcher.filters import state
from aiogram.dispatcher.filters.state import State

from keyboards.inline.plot_uz_reg import menu_plot_uz_muz, menu_plot_uz_qor
from keyboards.inline.plot_uz_uz import menu_plot_uz_zarafshon, menu_plot_uz_shim, menu_plot_uz_zarmitan, \
    menu_plot_uz_hisor, menu_plot_uz_surxon, menu_plot_uz_kuk
from loader import dp
from states.uz_states import menu_uz
from utils.list.app_list import app_list


@dp.callback_query_handler(text='expedition_uz:"Zarafshon" DGQE', state=menu_uz.expedition)
async def send_expedition(call: types.CallbackQuery):
    expedition = call.data.split(":")[1]
    app_list["expedition"] = expedition
    await call.message.delete()
    await call.message.answer("Uchastkani tanlang:", reply_markup=menu_plot_uz_zarafshon)
    await menu_uz.next()


@dp.callback_query_handler(text='expedition_uz:"Shimoliy Nurota" DGQE', state=menu_uz.expedition)
async def send_expedition(call: types.CallbackQuery):
    expedition = call.data.split(":")[1]
    app_list["expedition"] = expedition
    await call.message.delete()
    await call.message.answer("Uchastkani tanlang:", reply_markup=menu_plot_uz_shim)
    await menu_uz.next()


@dp.callback_query_handler(text='expedition_uz:"Zarmitan" DGQE', state=menu_uz.expedition)
async def send_expedition(call: types.CallbackQuery):
    expedition = call.data.split(":")[1]
    app_list["expedition"] = expedition
    await call.message.delete()
    await call.message.answer("Uchastkani tanlang:", reply_markup=menu_plot_uz_zarmitan)
    await menu_uz.next()


@dp.callback_query_handler(text='expedition_uz:"Hisor" DGQE', state=menu_uz.expedition)
async def send_expedition(call: types.CallbackQuery):
    expedition = call.data.split(":")[1]
    app_list["expedition"] = expedition
    await call.message.delete()
    await call.message.answer("Uchastkani tanlang:", reply_markup=menu_plot_uz_hisor)
    await menu_uz.next()


@dp.callback_query_handler(text='expedition_uz:"Surxon" DGQE', state=menu_uz.expedition)
async def send_expedition(call: types.CallbackQuery):
    expedition = call.data.split(":")[1]
    app_list["expedition"] = expedition
    await call.message.delete()
    await call.message.answer("Uchastkani tanlang:", reply_markup=menu_plot_uz_surxon)
    await menu_uz.next()


@dp.callback_query_handler(text='expedition_uz:"Kukpatas" DGQE', state=menu_uz.expedition)
async def send_expedition(call: types.CallbackQuery):
    expedition = call.data.split(":")[1]
    app_list["expedition"] = expedition
    await call.message.delete()
    await call.message.answer("Uchastkani tanlang:", reply_markup=menu_plot_uz_kuk)
    await menu_uz.next()


@dp.callback_query_handler(text='expedition_uz:"Daugiztau" DGQE', state=menu_uz.expedition)
async def send_expedition(call: types.callback_query):
    expedition = call.data.split(":")[1]
    app_list["expedition"] = expedition
    await call.answer("❌Uchastka mavjud emas", show_alert=True)


@dp.callback_query_handler(text='expedition_uz:"Markaziy '
                                'Uzbeksitan" DGTE', state=menu_uz.expedition)
async def send_expedition(call: types.CallbackQuery):
    expedition = call.data.split(":")[1]
    app_list["expedition"] = expedition
    await call.message.delete()
    await call.message.answer("Uchastkani tanlang:", reply_markup=menu_plot_uz_muz)
    await menu_uz.next()


@dp.callback_query_handler(text='expedition_uz:"Qoraqalpoq" DGTE', state=menu_uz.expedition)
async def send_expedition(call: types.CallbackQuery):
    expedition = call.data.split(":")[1]
    app_list["expedition"] = expedition
    await call.message.delete()
    await call.message.answer("Uchastkani tanlang:", reply_markup=menu_plot_uz_qor)
    await menu_uz.next()


@dp.callback_query_handler(text='expedition_uz:"Sharqiy Uzbekistan" '
                                'DGTE', state=menu_uz.expedition)
async def send_expedition(call: types.callback_query):
    expedition = call.data.split(":")[1]
    app_list["expedition"] = expedition
    await call.answer("❌Uchastka mavjud emas", show_alert=True)


@dp.callback_query_handler(text='expedition_uz:"Markaziy" GGE', state=menu_uz.expedition)
async def send_expedition(call: types.callback_query):
    expedition = call.data.split(":")[1]
    app_list["expedition"] = expedition
    await call.answer("❌Uchastka mavjud emas", show_alert=True)
