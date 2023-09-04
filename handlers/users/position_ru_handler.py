from aiogram import types

from keyboards.inline.method_uz import method_uz
from loader import dp
from states.ru_states import menu_ru
from states.uz_states import menu_uz
from utils.list.app_list import app_list


@dp.message_handler(state=menu_ru.position)
async def get_well_number(message: types.Message):
    position = message.text
    app_list["position"] = position
    await message.answer("Введите Государственный номер (12-123/12)")
    await menu_ru.next()
