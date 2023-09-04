from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from keyboards.default.lang_ru_button import menu_send_button_ru
from states.ru_states import menu_ru
from states.uz_states import menu_uz
from keyboards.inline.region_ru import menu_region_ru


from loader import dp, bot


@dp.message_handler(text="🇷🇺 Руский")
async def table_uz(message: types.Message):
    await message.answer("Выберите одну из кнопок🤳", reply_markup=menu_send_button_ru)
    await menu_ru.ru_lang.set()


@dp.message_handler(text="✍🏻 Разместить заказ", state=menu_ru.ru_lang)
async def send_application(message: types.Message):
    await message.answer("📍Выберите регион", reply_markup=menu_region_ru)
    await menu_ru.next()
