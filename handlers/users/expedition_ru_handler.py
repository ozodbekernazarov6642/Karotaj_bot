from aiogram import types
from aiogram.dispatcher.filters import state
from aiogram.dispatcher.filters.state import State

from keyboards.inline.plot_ru_reg import menu_plot_ru_qor, menu_plot_ru_muz
from keyboards.inline.plot_ru_uz import menu_plot_ru_zarafshon, menu_plot_ru_shim, menu_plot_ru_zarmitan, \
    menu_plot_ru_hisor, menu_plot_ru_surxon, menu_plot_ru_kuk
from keyboards.inline.plot_uz_uz import menu_plot_uz_zarafshon, menu_plot_uz_shim, menu_plot_uz_zarmitan, \
    menu_plot_uz_hisor, menu_plot_uz_surxon, menu_plot_uz_kuk
from loader import dp
from states.ru_states import menu_ru
from utils.list.app_list import app_list


@dp.callback_query_handler(text='expedition_ru:"Зарафшон" ДГҚЭ', state=menu_ru.expedition)
async def send_expedition(call: types.CallbackQuery):
    expedition = call.data.split(":")[1]
    app_list["expedition"] = expedition
    await call.message.delete()
    await call.message.answer("Выберите участка: ", reply_markup=menu_plot_ru_zarafshon)
    await menu_ru.next()


@dp.callback_query_handler(text='expedition_ru:"Шимолий Нурота" ДГҚЭ', state=menu_ru.expedition)
async def send_expedition(call: types.CallbackQuery):
    expedition = call.data.split(":")[1]
    app_list["expedition"] = expedition
    await call.message.delete()
    await call.message.answer("Выберите участка:", reply_markup=menu_plot_ru_shim)
    await menu_ru.next()


@dp.callback_query_handler(text='expedition_ru:"Зармитан" ДГҚЭ', state=menu_ru.expedition)
async def send_expedition(call: types.CallbackQuery):
    expedition = call.data.split(":")[1]
    app_list["expedition"] = expedition
    await call.message.delete()
    await call.message.answer("Выберите участка:", reply_markup=menu_plot_ru_zarmitan)
    await menu_ru.next()


@dp.callback_query_handler(text='expedition_ru:"Хисор" ДГҚЭ', state=menu_ru.expedition)
async def send_expedition(call: types.CallbackQuery):
    expedition = call.data.split(":")[1]
    app_list["expedition"] = expedition
    await call.message.delete()
    await call.message.answer("Выберите участка:", reply_markup=menu_plot_ru_hisor)
    await menu_ru.next()


@dp.callback_query_handler(text='expedition_ru:"Сурхон " ДГҚЭ', state=menu_ru.expedition)
async def send_expedition(call: types.CallbackQuery):
    expedition = call.data.split(":")[1]
    app_list["expedition"] = expedition
    await call.message.delete()
    await call.message.answer("Выберите участка:", reply_markup=menu_plot_ru_surxon)
    await menu_ru.next()


@dp.callback_query_handler(text='expedition_ru:"Кокпатас" ДГҚЭ', state=menu_ru.expedition)
async def send_expedition(call: types.CallbackQuery):
    expedition = call.data.split(":")[1]
    app_list["expedition"] = expedition
    await call.message.delete()
    await call.message.answer("Выберите участка:", reply_markup=menu_plot_ru_kuk)
    await menu_ru.next()


@dp.callback_query_handler(text='expedition_ru:"Даугизтау" ДГҚЭ', state=menu_ru.expedition)
async def send_expedition(call: types.callback_query):
    expedition = call.data.split(":")[1]
    app_list["expedition"] = expedition
    await call.answer("❌Участок недоступен", show_alert=True)


@dp.callback_query_handler(text='expedition_ru:"Марказий-Ўзбекистон" ДГТЭ', state=menu_ru.expedition)
async def send_expedition(call: types.CallbackQuery):
    expedition = call.data.split(":")[1]
    app_list["expedition"] = expedition
    await call.message.delete()
    await call.message.answer("Выберите участка:", reply_markup=menu_plot_ru_muz)
    await menu_ru.next()


@dp.callback_query_handler(text='expedition_ru:"Қорақалпоқ" ДГТЭ', state=menu_ru.expedition)
async def send_expedition(call: types.CallbackQuery):
    expedition = call.data.split(":")[1]
    app_list["expedition"] = expedition
    await call.message.delete()
    await call.message.answer("Выберите участка:", reply_markup=menu_plot_ru_qor)
    await menu_ru.next()


@dp.callback_query_handler(text='expedition_ru:"Шарқий-Ўзбекистон" ДГТЭ', state=menu_ru.expedition)
async def send_expedition(call: types.callback_query):
    expedition = call.data.split(":")[1]
    app_list["expedition"] = expedition
    await call.answer("❌Участок недоступен", show_alert=True)


@dp.callback_query_handler(text='expedition_ru:"Марказий" ГГЭ', state=menu_ru.expedition)
async def send_expedition(call: types.callback_query):
    expedition = call.data.split(":")[1]
    app_list["expedition"] = expedition
    await call.answer("❌Участок недоступен", show_alert=True)
