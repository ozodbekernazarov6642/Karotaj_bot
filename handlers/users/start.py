from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.language_button import menu_lang
from states.lang_state import Lang_state
from states.lang_state import Lang_state
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"<i>Assalomu aleykum, foydalanish tilini tanlang!</i> 👇\n"
                         f"___________________________________\n\n"
                         f"Здравствуйте, выбери свой язык 👇", reply_markup=menu_lang)


@dp.message_handler(CommandStart(), state=Lang_state.uzb)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(f"<i>Assalomu aleykum, foydalanish tilini tanlang!</i> 👇\n"
                         f"___________________________________\n\n"
                         f"Здравствуйте, выбери свой язык 👇", reply_markup=menu_lang)
    await state.finish()


@dp.message_handler(CommandStart(), state=Lang_state.ru)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(f"<i>Assalomu aleykum, foydalanish tilini tanlang!</i> 👇\n"
                         f"___________________________________\n\n"
                         f"Здравствуйте, выбери свой язык 👇", reply_markup=menu_lang)
    await state.finish()





