from aiogram import types

from loader import dp
from states.ru_states import menu_ru
from states.uz_states import menu_uz
from utils.list.app_list import app_list


@dp.message_handler(state=menu_ru.well_number)
async def get_well_number(message: types.Message):
    well_number = message.text
    app_list["well_number"] = well_number
    await message.answer("Введите глубину скважины:")
    await menu_ru.next()
