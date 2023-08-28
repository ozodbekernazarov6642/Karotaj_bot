from aiogram.dispatcher.filters import Text
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram import types
import re
from loader import dp
from states.uz_states import menu_uz
from utils.list.app_list import app_list


@dp.callback_query_handler(text="plot_uz:Salin", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer(f"Korxona nomi: " + app_list.get("region") + "\n"
                                                                           "Ekspeditsiya nomi: " + app_list.get(
        "expedition") + "\n"
                        "Uchastka nomi: " + app_list.get("plot"))
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Tashkan", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Yangi Davon (metro)", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Radjan (shimoliy)", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Yangi Davon (markaziy)", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Yangi Umid", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Yangi Davon", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Avliyo", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:G\'arbiy", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Gumsay", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Kuchumsay", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Lapak", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Ingichka", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Oltin Diyor", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Pistali", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:G\'arbiy Pistali", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:G\'arbiy Kosonsoy", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Zarmitan", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Markaziy", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Yuqori Saroy", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Bayram", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Davlatxo\'ja", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Tukman", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:O\'rtaliq", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Gujumsoy", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Xodjadiq", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Kamangaron", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Yaxton", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Iral", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Akba", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Sarikul", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Maydansan", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Nilu", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Shimoliy", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Shimoliy Chinorsoy", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Chalcharatau (K)", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Chalcharatau (Sh)", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Saridjoy (K)", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Saridjoy (Sh)", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Mingboy (Sh)", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Mingboy (K)", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Derbez (K)", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Derbez (Sh)", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Jetimtau (K)", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Jetimtau (Sh)", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Auminzatau GTP (K)", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Auminzatau GTP (Sh)", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Tamditau GTP (K)", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Tamditau GTP (Sh)", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Aristantov GTP (K)", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Aristantov GTP (Sh)", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Irlir", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Novkat", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Ulkentau", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Tas-Kazgan", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Quljiqtau", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()


@dp.callback_query_handler(text="plot_uz:Sulton Uvays", state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Quduq raqmini kiriting")
    await menu_uz.next()
