from aiogram import types

from keyboards.inline.method_uz import method_uz
from loader import dp
from states.uz_states import menu_uz
from utils.list.app_list import app_list


@dp.message_handler(state=menu_uz.position)
async def get_well_number(message: types.Message):
    position = message.text
    app_list["position"] = position
    await message.answer("Davlat raqamini kiritng")
    await menu_uz.next()
