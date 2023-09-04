from aiogram.dispatcher import FSMContext
from aiogram import types
from keyboards.default.language_button import menu_lang
from keyboards.default.lang_uz_button import menu_send_button_uz
from keyboards.inline.expedition_uz_reg import menu_expedition_uz_reg
from keyboards.inline.expedition_uz_uz import menu_expedition_uz_uz
from keyboards.inline.region_uz import menu_region_uz
from states.uz_states import menu_uz

from loader import dp


@dp.message_handler(text="⬅️ Ortga", state=menu_uz.uz_lang)
async def lang_back_uz(message: types.Message, state: FSMContext):
    await message.answer("🌐 Foydalanish tilini tanlang!👇\n"
                         "________________________________\n\n"
                         "🌐 Выбери свой язык 👇", reply_markup=menu_lang)
    await state.finish()


@dp.callback_query_handler(text="region_uz:back", state=menu_uz.region)
async def region_uz_back(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("Tugmalardan birini tanlang🤳", reply_markup=menu_send_button_uz)
    await menu_uz.previous()


@dp.callback_query_handler(text="expedition_uz:back", state=menu_uz.expedition)
async def expedition_uz_back(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Korxonani tanlang", reply_markup=menu_region_uz)
    await menu_uz.previous()


@dp.callback_query_handler(text="plot_uz_uz:back", state=menu_uz.plot)
async def plot_uz_back(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Ekspeditsiyani tanlang", reply_markup=menu_expedition_uz_uz)
    await menu_uz.previous()


@dp.callback_query_handler(text="plot_uz_reg:back", state=menu_uz.plot)
async def plot_uz_back(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Ekspeditsiyani tanlang", reply_markup=menu_expedition_uz_reg)
    await menu_uz.previous()


@dp.message_handler(text="⬆️ Bosh Menyu", state=menu_uz.well_number)
@dp.message_handler(text="⬆️ Bosh Menyu", state=menu_uz.depth)
@dp.message_handler(text="⬆️ Bosh Menyu", state=menu_uz.method)
@dp.message_handler(text="⬆️ Bosh Menyu", state=menu_uz.arrival_time)
@dp.message_handler(text="⬆️ Bosh Menyu", state=menu_uz.customer_name)
@dp.message_handler(text="⬆️ Bosh Menyu", state=menu_uz.position)
@dp.message_handler(text="⬆️ Bosh Menyu", state=menu_uz.state_number)
@dp.message_handler(text="⬆️ Bosh Menyu", state=menu_uz.drill_type)
@dp.message_handler(text="⬆️ Bosh Menyu", state=menu_uz.preparation_time)
@dp.message_handler(text="⬆️ Bosh Menyu", state=menu_uz.confirmation)
@dp.message_handler(text="⬆️ Bosh Menyu")
async def menu_back(message: types.Message, state: FSMContext):
    await message.answer("Tugmalardan birini tanlang🤳", reply_markup=menu_send_button_uz)
    await menu_uz.uz_lang.set()
