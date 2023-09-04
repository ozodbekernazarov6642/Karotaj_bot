from aiogram import types

from keyboards.inline.drill_type_uz import drill_type
from keyboards.inline.expedition_uz_reg import menu_expedition_uz_reg
from keyboards.inline.expedition_uz_uz import menu_expedition_uz_uz
# from keyboards.inline.preparation_time_ru import preparation_time
from loader import dp
from states.uz_states import menu_uz
from utils.list.app_list import app_list


@dp.callback_query_handler(text="K", state=menu_uz.drill_type)
async def send_expedition(call: types.CallbackQuery):
    app_list["drill_type"] = call.data
    await call.message.answer("Quduq tayyor bo'lish vaqtini tanlng", reply_markup=preparation_time)
    await call.message.delete()
    await menu_uz.next()


@dp.callback_query_handler(text="Sh", state=menu_uz.drill_type)
async def send_expedition(call: types.CallbackQuery):
    app_list["drill_type"] = call.data
    await call.message.answer("Quduq tayyor bo'lish vaqtini tanlng", reply_markup=preparation_time)
    await call.message.delete()
    await menu_uz.next()
