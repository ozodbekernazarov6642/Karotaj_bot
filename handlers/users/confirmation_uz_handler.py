from aiogram import types

import states.uz_states
from keyboards.inline.drill_type_uz import drill_type
from keyboards.inline.expedition_uz_reg import menu_expedition_uz_reg
from keyboards.inline.expedition_uz_uz import menu_expedition_uz_uz
from keyboards.inline.preparation_time_uz import preparation_time
from loader import dp
from states.uz_states import menu_uz
from utils.list.app_list import app_list


@dp.callback_query_handler(text="confirmation", state=menu_uz.confirmation)
async def send_confirmation(call: types.CallbackQuery):
    await call.message.answer("Ariza tasdiqlandi!")
    await call.message.delete()
    await states.uz_states.menu_uz.first()
