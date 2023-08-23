from aiogram.dispatcher import FSMContext
from aiogram import types
from keyboards.default.language_button import menu_lang
from keyboards.default.lang_uz_button import menu_send_button_uz
from states.lang_state import Lang_state

from loader import dp

@dp.message_handler(text="⬅️ Ortga", state=Lang_state.uzb)
async def lang_back_uz(message: types.Message, state: FSMContext):
    await message.answer("🌐 Foydalanish tilini tanlang!👇\n"
                         "________________________________\n\n"
                         "🌐 Выбери свой язык 👇", reply_markup=menu_lang)
    await state.finish()


@dp.message_handler(text="⬅️ Назад", state=Lang_state.ru)
async def lang_back_uz(message: types.Message, state: FSMContext):
    await message.answer("🌐 Foydalanish tilini tanlang!👇\n"
                         "________________________________\n\n"
                         "🌐 Выбери свой язык 👇", reply_markup=menu_lang)
    await state.finish()



@dp.callback_query_handler(text="region_uz:back", state=Lang_state.uzb)
async def region_uz_back(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Tugmalardan birini tanlang🤳", reply_markup=menu_send_button_uz)






