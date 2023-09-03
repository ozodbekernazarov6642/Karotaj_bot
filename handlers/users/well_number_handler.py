from aiogram import types

from loader import dp
from states.uz_states import menu_uz
from utils.list.app_list import app_list


@dp.message_handler(state=menu_uz.well_number)
async def get_well_number(message: types.Message):
    well_number = message.text
    app_list["well_number"] = well_number
    await message.answer("Quduq chuqurligini kiriting")
    await menu_uz.next()
