from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.language_button import menu_lang
from states.ru_states import menu_ru
from states.uz_states import menu_uz
from loader import dp


@dp.message_handler(CommandStart())
@dp.message_handler(CommandStart(), state=menu_uz.uz_lang)
@dp.message_handler(CommandStart(), state=menu_uz.region)
@dp.message_handler(CommandStart(), state=menu_uz.expedition)
@dp.message_handler(CommandStart(), state=menu_uz.plot)
@dp.message_handler(CommandStart(), state=menu_uz.well_number)
@dp.message_handler(CommandStart(), state=menu_uz.depth)
@dp.message_handler(CommandStart(), state=menu_uz.method)
@dp.message_handler(CommandStart(), state=menu_uz.arrival_time)
@dp.message_handler(CommandStart(), state=menu_uz.customer_name)
@dp.message_handler(CommandStart(), state=menu_uz.position)
@dp.message_handler(CommandStart(), state=menu_uz.state_number)
@dp.message_handler(CommandStart(), state=menu_uz.drill_type)
@dp.message_handler(CommandStart(), state=menu_uz.expedition)
@dp.message_handler(CommandStart(), state=menu_uz.confirmation)
@dp.message_handler(CommandStart(), state=menu_ru.ru_lang)
@dp.message_handler(CommandStart(), state=menu_ru.region)
@dp.message_handler(CommandStart(), state=menu_ru.expedition)
@dp.message_handler(CommandStart(), state=menu_ru.plot)
@dp.message_handler(CommandStart(), state=menu_ru.well_number)
@dp.message_handler(CommandStart(), state=menu_ru.depth)
@dp.message_handler(CommandStart(), state=menu_ru.method)
@dp.message_handler(CommandStart(), state=menu_ru.arrival_time)
@dp.message_handler(CommandStart(), state=menu_ru.customer_name)
@dp.message_handler(CommandStart(), state=menu_ru.position)
@dp.message_handler(CommandStart(), state=menu_ru.state_number)
@dp.message_handler(CommandStart(), state=menu_ru.drill_type)
@dp.message_handler(CommandStart(), state=menu_ru.expedition)
@dp.message_handler(CommandStart(), state=menu_ru.confirmation)
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer(f"<i>Assalomu aleykum, foydalanish tilini tanlang!</i> 👇\n"
                         f"___________________________________\n\n"
                         f"Здравствуйте, выбери свой язык 👇", reply_markup=menu_lang)
    await state.finish()
