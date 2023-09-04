import re

from aiogram import types

from keyboards.inline.drill_type_ru import drill_type_ru
from keyboards.inline.drill_type_uz import drill_type
from loader import dp
from states.ru_states import menu_ru
from states.uz_states import menu_uz
from utils.list.app_list import app_list


def use_regex(input_text):
    pattern = re.compile(r"\d\d-\d\d\d/\d\d", re.IGNORECASE)
    return pattern.match(input_text)


@dp.message_handler(state=menu_ru.state_number)
async def get_well_number(message: types.Message):
    state_number = message.text
    if use_regex(state_number):
        app_list["state_number"] = state_number
        await message.answer("Выберите тип сверла", reply_markup=drill_type_ru)
        await menu_ru.next()
    else:
        await message.reply("Введите как в примере")
