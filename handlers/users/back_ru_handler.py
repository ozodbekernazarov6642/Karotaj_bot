from aiogram.dispatcher import FSMContext
from aiogram import types

from keyboards.default.lang_ru_button import menu_send_button_ru
from keyboards.default.lang_uz_button import menu_send_button_uz
from states.lang_state import Lang_state

from loader import dp


@dp.callback_query_handler(text="region_ru:back", state=Lang_state.ru)
async def region_uz_back(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Выберите одну из кнопок🤳", reply_markup=menu_send_button_ru)