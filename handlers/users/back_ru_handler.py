from aiogram.dispatcher import FSMContext
from aiogram import types

from keyboards.default.lang_ru_button import menu_send_button_ru
from keyboards.default.language_button import menu_lang
from keyboards.inline.expedition_ru_reg import menu_expedition_ru_reg
from keyboards.inline.expedition_ru_uz import menu_expedition_ru_uz
from keyboards.inline.region_uz import menu_region_uz
from states.ru_states import menu_ru
from states.uz_states import menu_uz

from loader import dp


@dp.message_handler(text="⬅️ Назад", state=menu_ru.ru_lang)
async def lang_back_uz(message: types.Message, state: FSMContext):
    await message.answer("🌐 Foydalanish tilini tanlang!👇\n"
                         "________________________________\n\n"
                         "🌐 Выбери свой язык 👇", reply_markup=menu_lang)
    await state.finish()


@dp.callback_query_handler(text="region_ru:back", state=menu_ru.region)
async def region_ru_back(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("Выберите одну из кнопок🤳", reply_markup=menu_send_button_ru)
    await menu_ru.previous()


@dp.callback_query_handler(text="expedition_ru:back", state=menu_ru.expedition)
async def expedition_ru_back(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Выберите предприятие", reply_markup=menu_region_uz)
    await menu_ru.previous()


@dp.callback_query_handler(text="plot_ru_uz:back", state=menu_ru.plot)
async def plot_ru_back(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Выберите экспедицию", reply_markup=menu_expedition_ru_uz)
    await menu_ru.previous()


@dp.callback_query_handler(text="plot_ru_reg:back", state=menu_ru.plot)
async def plot_ru_back(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Выберите экспедицию", reply_markup=menu_expedition_ru_reg)
    await menu_ru.previous()


@dp.message_handler(text="⬆️ Главное меню", state=menu_ru.well_number)
@dp.message_handler(text="⬆️ Главное меню", state=menu_ru.depth)
@dp.message_handler(text="⬆️ Главное меню", state=menu_ru.method)
@dp.message_handler(text="⬆️ Главное меню", state=menu_ru.arrival_time)
@dp.message_handler(text="⬆️ Главное меню", state=menu_ru.customer_name)
@dp.message_handler(text="⬆️ Главное меню", state=menu_ru.position)
@dp.message_handler(text="⬆️ Главное меню", state=menu_ru.state_number)
@dp.message_handler(text="⬆️ Главное меню", state=menu_ru.drill_type)
@dp.message_handler(text="⬆️ Главное меню", state=menu_ru.preparation_time)
@dp.message_handler(text="⬆️ Главное меню", state=menu_ru.confirmation)
@dp.message_handler(text="⬆️ Главное меню")
async def menu_back(message: types.Message, state: FSMContext):
    await message.answer("Выберите одну из кнопок🤳", reply_markup=menu_send_button_ru)
    await menu_ru.ru_lang.set()
