from aiogram import types

from keyboards.inline.confirmation_uz import confirmation_uz
from loader import dp
from states.uz_states import menu_uz
from utils.list.app_list import app_list
from utils.time_Tashkent import time


@dp.callback_query_handler(text="Tayyor", state=menu_uz.preparation_time)
async def send_preparation_time(call: types.CallbackQuery):
    app_list["preparation_time"] = call.data
    time1 = await time()
    await call.message.answer(text=(
        f"🔰 Korxona nomi: {app_list.get('region')}\n\n"
        f"🔍 Ekspeditsiya nomi: {app_list.get('expedition')}\n\n"
        f"📍 Uchastka nomi: { app_list.get('plot')}\n\n"
        f"⛏️ Quduq raqami: {app_list.get('well_number')}\n\n"
        f"📏 Quduq chuqurligi: {app_list.get('depth')}\n\n"
        f"📝 Metod: {app_list.get('method')}\n\n"
        f"🚚 Yetib borish sanasi: {app_list.get('arrival_time')}\n\n"
        f"🕵️‍♂️ Buyurtmachi ismi: {app_list.get('customer_name')}\n\n"
        f"🪑 Buyurtmachi lavozimi: {app_list.get('position')}\n\n"
        f"🔢 Davlat raqami: {app_list.get('state_number')}\n\n"
        f"🧨 Burg'u turi: {app_list.get('drill_type')}\n\n"
        f"🕠 Quduq tayyor bo'lish vaqti: {app_list.get('preparation_time')}"), reply_markup=confirmation_uz)
    await call.message.delete()
    await menu_uz.next()


@dp.callback_query_handler(text="3 soat", state=menu_uz.preparation_time)
async def send_preparation_time(call: types.CallbackQuery):
    app_list["preparation_time"] = call.data
    time1 = await time()
    await call.message.answer(text=(
        f"🔰 Korxona nomi: {app_list.get('region')}\n\n"
        f"🔍 Ekspeditsiya nomi: {app_list.get('expedition')}\n\n"
        f"📍 Uchastka nomi: { app_list.get('plot')}\n\n"
        f"⛏️ Quduq raqami: {app_list.get('well_number')}\n\n"
        f"📏 Quduq chuqurligi: {app_list.get('depth')}\n\n"
        f"📝 Metod: {app_list.get('method')}\n\n"
        f"🚚 Yetib borish sanasi: {app_list.get('arrival_time')}\n\n"
        f"🕵️‍♂️ Buyurtmachi ismi: {app_list.get('customer_name')}\n\n"
        f"🪑 Buyurtmachi lavozimi: {app_list.get('position')}\n\n"
        f"🔢 Davlat raqami: {app_list.get('state_number')}\n\n"
        f"🧨 Burg'u turi:{app_list.get('drill_type')}\n\n"
        f"🕠 Quduq tayyor bo'lish vaqti: {app_list.get('preparation_time')}"), reply_markup=confirmation_uz)
    await call.message.delete()
    await menu_uz.next()


@dp.callback_query_handler(text="5 soat", state=menu_uz.preparation_time)
async def send_preparation_time(call: types.CallbackQuery):
    app_list["preparation_time"] = call.data
    time1 = await time()
    await call.message.answer(text=(
        f"🔰 Korxona nomi: {app_list.get('region')}\n\n"
        f"🔍 Ekspeditsiya nomi: {app_list.get('expedition')}\n\n"
        f"📍 Uchastka nomi: { app_list.get('plot')}\n\n"
        f"⛏️ Quduq raqami: {app_list.get('well_number')}\n\n"
        f"📏 Quduq chuqurligi: {app_list.get('depth')}\n\n"
        f"📝 Metod: {app_list.get('method')}\n\n"
        f"🚚 Yetib borish sanasi: {app_list.get('arrival_time')}\n\n"
        f"🕵️‍♂️ Buyurtmachi ismi: {app_list.get('customer_name')}\n\n"
        f"🪑 Buyurtmachi lavozimi: {app_list.get('position')}\n\n"
        f"🔢 Davlat raqami: {app_list.get('state_number')}\n\n"
        f"🧨 Burg'u turi:{app_list.get('drill_type')}\n\n"
        f"🕠 Quduq tayyor bo'lish vaqti: {app_list.get('preparation_time')}"), reply_markup=confirmation_uz)
    await call.message.delete()
    await menu_uz.next()


@dp.callback_query_handler(text="10 soat", state=menu_uz.preparation_time)
async def send_preparation_time(call: types.CallbackQuery):
    app_list["preparation_time"] = call.data
    time1 = await time()
    await call.message.answer(text=(
        f"🔰 Korxona nomi: {app_list.get('region')}\n\n"
        f"🔍 Ekspeditsiya nomi: {app_list.get('expedition')}\n\n"
        f"📍 Uchastka nomi: { app_list.get('plot')}\n\n"
        f"⛏️ Quduq raqami: {app_list.get('well_number')}\n\n"
        f"📏 Quduq chuqurligi: {app_list.get('depth')}\n\n"
        f"📝 Metod: {app_list.get('method')}\n\n"
        f"🚚 Yetib borish sanasi: {app_list.get('arrival_time')}\n\n"
        f"🕵️‍♂️ Buyurtmachi ismi: {app_list.get('customer_name')}\n\n"
        f"🪑 Buyurtmachi lavozimi: {app_list.get('position')}\n\n"
        f"🔢 Davlat raqami: {app_list.get('state_number')}\n\n"
        f"🧨 Burg'u turi:{app_list.get('drill_type')}\n\n"
        f"🕠 Quduq tayyor bo'lish vaqti: {app_list.get('preparation_time')}"), reply_markup=confirmation_uz)
    await call.message.delete()
    await menu_uz.next()




