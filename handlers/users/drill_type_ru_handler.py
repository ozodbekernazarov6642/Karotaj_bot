from aiogram import types

from keyboards.inline.drill_type_uz import drill_type
from keyboards.inline.expedition_uz_reg import menu_expedition_uz_reg
from keyboards.inline.expedition_uz_uz import menu_expedition_uz_uz
from keyboards.inline.preparation_time_ru import preparation_time_ru
# from keyboards.inline.preparation_time_ru import preparation_time, preparation_time_ru
from loader import dp
from states.ru_states import menu_ru
from states.uz_states import menu_uz
from utils.list.app_list import app_list


@dp.callback_query_handler(text="К", state=menu_ru.drill_type)
async def send_expedition(call: types.CallbackQuery):
    app_list["drill_type"] = call.data
    await call.message.answer("Выберите время, когда скважина будет готова", reply_markup=preparation_time_ru)
    await call.message.delete()
    await menu_ru.next()


@dp.callback_query_handler(text="Ш", state=menu_ru.drill_type)
async def send_expedition(call: types.CallbackQuery):
    app_list["drill_type"] = call.data
    await call.message.answer("Выберите время, когда скважина будет готова", reply_markup=preparation_time_ru)
    await call.message.delete()
    await menu_ru.next()
