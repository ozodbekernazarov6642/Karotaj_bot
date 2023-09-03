from aiogram import types

from keyboards.inline.method_uz import method_uz
from loader import dp
from states.uz_states import menu_uz
from utils.list.app_list import app_list


@dp.message_handler(state=menu_uz.customer_name)
async def get_well_number(message: types.Message):
    customer_name = message.text
    app_list["customer_name"] = customer_name
    await message.answer("Lavozimini kiriting")
    await menu_uz.next()
