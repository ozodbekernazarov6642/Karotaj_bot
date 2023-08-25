from aiogram.dispatcher import FSMContext
from aiogram import types

from keyboards.default.lang_ru_button import menu_send_button_ru
from keyboards.default.lang_uz_button import menu_send_button_uz
from keyboards.default.language_button import menu_lang
from keyboards.inline.expedition_ru_reg import menu_expedition_ru_reg
from keyboards.inline.expedition_ru_uz import menu_expedition_ru_uz
from keyboards.inline.region_ru import menu_region_ru
from keyboards.inline.region_uz import menu_region_uz
from states.lang_state import Lang_state

from loader import dp


@dp.callback_query_handler(text="region_ru:back", state=Lang_state.ru)
async def region_uz_back(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Выберите одну из кнопок🤳", reply_markup=menu_send_button_ru)


@dp.message_handler(text="⬅️ Назад", state=Lang_state.ru)
async def lang_back_uz(message: types.Message, state: FSMContext):
    await message.answer("🌐 Foydalanish tilini tanlang!👇\n"
                         "________________________________\n\n"
                         "🌐 Выбери свой язык 👇", reply_markup=menu_lang)

    await state.finish()


@dp.callback_query_handler(text="expedition_ru:back", state=Lang_state.ru)
async def expedition_uz_back(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Выберите предприятие", reply_markup=menu_region_ru)


@dp.callback_query_handler(text="plot_ru_uz:back", state=Lang_state.ru)
async def plot_uz_back(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Выберите экспедицию", reply_markup=menu_expedition_ru_uz)


@dp.callback_query_handler(text="plot_ru_reg:back", state=Lang_state.ru)
async def plot_uz_back(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Выберите экспедицию", reply_markup=menu_expedition_ru_reg)
