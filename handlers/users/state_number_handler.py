import re

from aiogram import types

from keyboards.inline.drill_type_uz import drill_type
from keyboards.inline.method_uz import method_uz
from keyboards.inline.preparation_time_uz import preparation_time
from loader import dp
from states.uz_states import menu_uz
from utils.list.app_list import app_list


def use_regex(input_text):
    pattern = re.compile(r"\d\d-\d\d\d/\d\d", re.IGNORECASE)
    return pattern.match(input_text)


@dp.message_handler(state=menu_uz.state_number)
async def get_well_number(message: types.Message):
    state_number = message.text
    if use_regex(state_number):
        app_list["state_number"] = state_number
        await message.answer("Burg'u turini tanlang", reply_markup=drill_type)
        await menu_uz.next()
    else:
        await message.reply("Namunadagidek kiriting")
