from aiogram import types

from keyboards.inline.confirmation_ru import confirmation_ru
from loader import dp
from states.ru_states import menu_ru
from utils.list.app_list import app_list
from utils.time_Tashkent import time


@dp.callback_query_handler(text="Готовый", state=menu_ru.preparation_time)
async def send_preparation_time(call: types.CallbackQuery):
    app_list["preparation_time"] = call.data
    time1 = await time()
    await call.message.answer(text=(
        f"🔰 Название компании: {app_list.get('region')}\n\n"
        f"🔍 Название экспедиции: {app_list.get('expedition')}\n\n"
        f"📍 Название участка: {app_list.get('plot')}\n\n"
        f"⛏️ Номер скважины: {app_list.get('well_number')}\n\n"
        f"📏 Глубина скважины: {app_list.get('depth')}\n\n"
        f"📝 Метод: {app_list.get('method')}\n\n"
        f"🚚 Дата прибытия: {app_list.get('arrival_time')}\n\n"
        f"🕵️‍♂️ Имя заказчика: {app_list.get('customer_name')}\n\n"
        f"🪑 Позиция заказчика: {app_list.get('position')}\n\n"
        f"🔢 Государственный номер: {app_list.get('state_number')}\n\n"
        f"🧨 Тип сверла: {app_list.get('drill_type')}\n\n"
        f"🕠 Пора подготовить скважины: {app_list.get('preparation_time')}"), reply_markup=confirmation_ru)
    await call.message.delete()
    await menu_ru.next()


@dp.callback_query_handler(text="3 час", state=menu_ru.preparation_time)
async def send_preparation_time(call: types.CallbackQuery):
    app_list["preparation_time"] = call.data
    time1 = await time()
    await call.message.answer(text=(
        f"🔰 Название компании: {app_list.get('region')}\n\n"
        f"🔍 Название экспедиции: {app_list.get('expedition')}\n\n"
        f"📍 Название участка: {app_list.get('plot')}\n\n"
        f"⛏️ Номер скважины: {app_list.get('well_number')}\n\n"
        f"📏 Глубина скважины: {app_list.get('depth')}\n\n"
        f"📝 Метод: {app_list.get('method')}\n\n"
        f"🚚 Дата прибытия: {app_list.get('arrival_time')}\n\n"
        f"🕵️‍♂️ Имя заказчика: {app_list.get('customer_name')}\n\n"
        f"🪑 Позиция заказчика: {app_list.get('position')}\n\n"
        f"🔢 Государственный номер: {app_list.get('state_number')}\n\n"
        f"🧨 Тип сверла:{app_list.get('drill_type')}\n\n"
        f"🕠 Пора подготовить скважины: {app_list.get('preparation_time')}"), reply_markup=confirmation_ru)
    await call.message.delete()
    await menu_ru.next()


@dp.callback_query_handler(text="5 час", state=menu_ru.preparation_time)
async def send_preparation_time(call: types.CallbackQuery):
    app_list["preparation_time"] = call.data
    time1 = await time()
    await call.message.answer(text=(
        f"🔰 Название компании: {app_list.get('region')}\n\n"
        f"🔍 Название экспедиции: {app_list.get('expedition')}\n\n"
        f"📍 Название участка: {app_list.get('plot')}\n\n"
        f"⛏️ Номер скважины: {app_list.get('well_number')}\n\n"
        f"📏 Глубина скважины: {app_list.get('depth')}\n\n"
        f"📝 Метод: {app_list.get('method')}\n\n"
        f"🚚 Дата прибытия: {app_list.get('arrival_time')}\n\n"
        f"🕵️‍♂️ Имя заказчика: {app_list.get('customer_name')}\n\n"
        f"🪑 Позиция заказчика: {app_list.get('position')}\n\n"
        f"🔢 Государственный номер: {app_list.get('state_number')}\n\n"
        f"🧨 Тип сверла:{app_list.get('drill_type')}\n\n"
        f"🕠 Пора подготовить скважины: {app_list.get('preparation_time')}"), reply_markup=confirmation_ru)
    await call.message.delete()
    await menu_ru.next()


@dp.callback_query_handler(text="10 час", state=menu_ru.preparation_time)
async def send_preparation_time(call: types.CallbackQuery):
    app_list["preparation_time"] = call.data
    time1 = await time()
    await call.message.answer(text=(
        f"🔰 Название компании: {app_list.get('region')}\n\n"
        f"🔍 Название экспедиции: {app_list.get('expedition')}\n\n"
        f"📍 Название участка: {app_list.get('plot')}\n\n"
        f"⛏️ Номер скважины: {app_list.get('well_number')}\n\n"
        f"📏 Глубина скважины: {app_list.get('depth')}\n\n"
        f"📝 Метод: {app_list.get('method')}\n\n"
        f"🚚 Дата прибытия: {app_list.get('arrival_time')}\n\n"
        f"🕵️‍♂️ Имя заказчика: {app_list.get('customer_name')}\n\n"
        f"🪑 Позиция заказчика: {app_list.get('position')}\n\n"
        f"🔢 Государственный номер: {app_list.get('state_number')}\n\n"
        f"🧨 Тип сверла:{app_list.get('drill_type')}\n\n"
        f"🕠 Пора подготовить скважины: {app_list.get('preparation_time')}"), reply_markup=confirmation_ru)
    await call.message.delete()
    await menu_ru.next()




