from aiogram.dispatcher import FSMContext
from aiogram import types
from keyboards.default.language_button import menu_lang
from keyboards.default.lang_uz_button import menu_send_button_uz
from keyboards.inline.expedition_uz_reg import menu_expedition_uz_reg
from keyboards.inline.expedition_uz_uz import menu_expedition_uz_uz
from keyboards.inline.region_uz import menu_region_uz
from states.lang_state import Lang_state

from loader import dp


@dp.message_handler(text="⬅️ Ortga", state=Lang_state.uzb)
async def lang_back_uz(message: types.Message, state: FSMContext):
    await message.answer("🌐 Foydalanish tilini tanlang!👇\n"
                         "________________________________\n\n"
                         "🌐 Выбери свой язык 👇", reply_markup=menu_lang)
    await state.finish()


@dp.callback_query_handler(text="region_uz:back", state=Lang_state.uzb)
async def region_uz_back(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Tugmalardan birini tanlang🤳", reply_markup=menu_send_button_uz)


@dp.callback_query_handler(text="expedition_uz:back", state=Lang_state.uzb)
async def expedition_uz_back(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Korxonani tanlang", reply_markup=menu_region_uz)


@dp.callback_query_handler(text="plot_uz_uz:back", state=Lang_state.uzb)
async def plot_uz_back(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Ekspeditsiyani tanlang", reply_markup=menu_expedition_uz_uz)


@dp.callback_query_handler(text="plot_uz_reg:back", state=Lang_state.uzb)
async def plot_uz_back(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Ekspeditsiyani tanlang", reply_markup=menu_expedition_uz_reg)
