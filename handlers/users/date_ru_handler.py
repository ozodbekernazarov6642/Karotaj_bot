import re

from aiogram import types

from loader import dp
from states.ru_states import menu_ru
from states.uz_states import menu_uz
from utils.list.app_list import app_list


def use_regex(input_text):
    pattern = re.compile(r"\d\d/\d\d/\d\d\d\d", re.IGNORECASE)
    return pattern.match(input_text)


@dp.message_handler(state=menu_ru.arrival_time)
async def get_well_number(message: types.Message):
    arrival_time = message.text
    if use_regex(arrival_time):
        app_list["arrival_time"] = arrival_time
        await message.answer("Введите имя заказчика (Ф.И.O)")
        await menu_ru.next()
    else:
        await message.reply("Введите время как в примере!")
