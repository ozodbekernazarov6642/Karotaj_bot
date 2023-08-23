from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from keyboards.default.lang_uz_button import menu_send_button_uz
from states.lang_state import Lang_state
from keyboards.inline.region_uz_InlineKeyboard import menu_region_uz

from loader import dp, bot


@dp.message_handler(text="🇺🇿 O'zbekcha")
async def table_uz(message: types.Message):
    await message.answer("Tugmalardan birini tanlang🤳", reply_markup=menu_send_button_uz)
    await Lang_state.uzb.set()


@dp.message_handler(text="✍🏻 Buyurtma berish", state=Lang_state.uzb)
async def send_application(message: types.Message):
    await message.answer("Buyurtma Hududni tanlang", reply_markup=menu_region_uz)



