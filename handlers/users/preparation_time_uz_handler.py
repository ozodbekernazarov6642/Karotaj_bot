from aiogram import types

from keyboards.inline.confirmation_uz import confirmation
from keyboards.inline.drill_type_uz import drill_type
from keyboards.inline.expedition_uz_reg import menu_expedition_uz_reg
from keyboards.inline.expedition_uz_uz import menu_expedition_uz_uz
from keyboards.inline.preparation_time_uz import preparation_time
from loader import dp
from states.uz_states import menu_uz
from utils.list.app_list import app_list


@dp.callback_query_handler(text="Tayyor", state=menu_uz.preparation_time)
async def send_preparation_time(call: types.CallbackQuery):
    app_list["preparation_time"] = call.data
    await call.message.answer(f"Korxona nomi: " + app_list.get("region") + "\n"
                                                                           "Ekspeditsiya nomi: " + app_list.get(
        "expedition") + "\n"
                        "Uchastka nomi: " + app_list.get("plot") + "\n"
                                                                   "Quduq raqami: " + app_list.get("well_number") + "\n"
                                                                                                                    "Quduq chuqurligi: " + app_list.get(
        "depth") + "\n"
                   "Metod: " + app_list.get("method") + "\n"
                                                        "Yetib borish sanasi:" + app_list.get("arrival_time") + "\n"
                                                                                                                "Buyurtmachi ismi:" + app_list.get(
        "customer_name") + "\n"
                           "Buyurtmachi lavozimi: " + app_list.get("position") + "\n"
                                                                                 "Davlat raqami: " + app_list.get(
        "state_number") + "\n"
                          "Burg'u turi: " + app_list.get("drill_type") + "\n"
                                                                         "Quduq tayyor bo'lish vaqti: " + app_list.get(
        "preparation_time"), reply_markup=confirmation)
    await call.message.delete()
    await menu_uz.next()


@dp.callback_query_handler(text="3 soat", state=menu_uz.preparation_time)
async def send_preparation_time(call: types.CallbackQuery):
    app_list["preparation_time"] = call.data
    await call.message.answer(f"Korxona nomi: " + app_list.get("region") + "\n"
                                                                           "Ekspeditsiya nomi: " + app_list.get(
        "expedition") + "\n"
                        "Uchastka nomi: " + app_list.get("plot") + "\n"
                                                                   "Quduq raqami: " + app_list.get("well_number") + "\n"
                                                                                                                    "Quduq chuqurligi: " + app_list.get(
        "depth") + "\n"
                   "Metod: " + app_list.get("method") + "\n"
                                                        "Yetib borish sanasi:" + app_list.get("arrival_time") + "\n"
                                                                                                                "Buyurtmachi ismi:" + app_list.get(
        "customer_name") + "\n"
                           "Buyurtmachi lavozimi: " + app_list.get("position") + "\n"
                                                                                 "Davlat raqami: " + app_list.get(
        "state_number") + "\n"
                          "Burg'u turi: " + app_list.get("drill_type") + "\n"
                                                                         "Quduq tayyor bo'lish vaqti: " + app_list.get(
        "preparation_time"), reply_markup=confirmation)
    await call.message.delete()
    await menu_uz.next()


@dp.callback_query_handler(text="5 soat", state=menu_uz.preparation_time)
async def send_preparation_time(call: types.CallbackQuery):
    app_list["preparation_time"] = call.data
    await call.message.answer(f"Korxona nomi: " + app_list.get("region") + "\n"
                                                                           "Ekspeditsiya nomi: " + app_list.get(
        "expedition") + "\n"
                        "Uchastka nomi: " + app_list.get("plot") + "\n"
                                                                   "Quduq raqami: " + app_list.get("well_number") + "\n"
                                                                                                                    "Quduq chuqurligi: " + app_list.get(
        "depth") + "\n"
                   "Metod: " + app_list.get("method") + "\n"
                                                        "Yetib borish sanasi:" + app_list.get("arrival_time") + "\n"
                                                                                                                "Buyurtmachi ismi:" + app_list.get(
        "customer_name") + "\n"
                           "Buyurtmachi lavozimi: " + app_list.get("position") + "\n"
                                                                                 "Davlat raqami: " + app_list.get(
        "state_number") + "\n"
                          "Burg'u turi: " + app_list.get("drill_type") + "\n"
                                                                         "Quduq tayyor bo'lish vaqti: " + app_list.get(
        "preparation_time"), reply_markup=confirmation)
    await call.message.delete()
    await menu_uz.next()


@dp.callback_query_handler(text="10 soat", state=menu_uz.preparation_time)
async def send_preparation_time(call: types.CallbackQuery):
    app_list["preparation_time"] = call.data
    await call.message.answer(f"Korxona nomi: " + app_list.get("region") + "\n"
                                                                           "Ekspeditsiya nomi: " + app_list.get(
        "expedition") + "\n"
                        "Uchastka nomi: " + app_list.get("plot") + "\n"
                                                                   "Quduq raqami: " + app_list.get("well_number") + "\n"
                                                                                                                    "Quduq chuqurligi: " + app_list.get(
        "depth") + "\n"
                   "Metod: " + app_list.get("method") + "\n"
                                                        "Yetib borish sanasi:" + app_list.get("arrival_time") + "\n"
                                                                                                                "Buyurtmachi ismi:" + app_list.get(
        "customer_name") + "\n"
                           "Buyurtmachi lavozimi: " + app_list.get("position") + "\n"
                                                                                 "Davlat raqami: " + app_list.get(
        "state_number") + "\n"
                          "Burg'u turi: " + app_list.get("drill_type") + "\n"
                                                                         "Quduq tayyor bo'lish vaqti: " + app_list.get(
        "preparation_time"), reply_markup=confirmation)
    await call.message.delete()
    await menu_uz.next()
