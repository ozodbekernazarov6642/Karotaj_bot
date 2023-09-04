from aiogram import types

from keyboards.inline.method_uz import method_uz
from loader import dp
from states.uz_states import menu_uz
from utils.list.app_list import app_list


@dp.message_handler(state=menu_uz.depth)
async def get_well_number(message: types.Message):
    depth = message.text
    app_list["depth"] = depth
    await message.answer("Metodni tanlang:", reply_markup=method_uz)
    await menu_uz.next()
