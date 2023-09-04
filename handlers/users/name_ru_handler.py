from aiogram import types

from keyboards.inline.method_uz import method_uz
from loader import dp
from states.ru_states import menu_ru
from utils.list.app_list import app_list


@dp.message_handler(state=menu_ru.customer_name)
async def get_well_number(message: types.Message):
    customer_name = message.text
    app_list["customer_name"] = customer_name
    await message.answer("Введите позицию")
    await menu_ru.next()
