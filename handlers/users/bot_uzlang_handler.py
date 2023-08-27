from aiogram import types
from keyboards.default.lang_uz_button import menu_send_button_uz
from states.uz_states import menu_uz
from keyboards.inline.region_uz import menu_region_uz

from loader import dp


@dp.message_handler(text="🇺🇿 O'zbekcha")
async def table_uz(message: types.Message):
    await message.answer("Tugmalardan birini tanlang🤳", reply_markup=menu_send_button_uz)
    await menu_uz.uz_lang.set()


@dp.message_handler(text="✍🏻 Buyurtma berish", state=menu_uz.uz_lang)
async def send_application(message: types.Message):
    await message.answer("Buyurtma Hududni tanlang", reply_markup=menu_region_uz)





