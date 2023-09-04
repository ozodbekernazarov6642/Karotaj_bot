from aiogram import types

from keyboards.inline.method_ru import method_ru
from loader import dp
from states.ru_states import menu_ru
from states.uz_states import menu_uz
from utils.list.app_list import app_list


@dp.message_handler(state=menu_ru.depth)
async def get_well_number(message: types.Message):
    depth = message.text
    app_list["depth"] = depth
    await message.answer("Выберите метод:", reply_markup=method_ru)
    await menu_ru.next()
