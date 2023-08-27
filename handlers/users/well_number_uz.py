from aiogram.dispatcher.filters import Text
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram import types
import re
from loader import dp
from states.uz_states import menu_uz


@dp.callback_query_handler(Text(startswith='plot_uz'), state=menu_uz.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer(f"Quduq raqamini kiriting 👇")
    await menu_uz.next()


@dp.message_handler(Text(startswith="Quduq raqmini"), state=menu_uz.depth)
async def well_number_uz_check(message: types.Message):
    pattern = r"^[1-9]\d{4}$"
    try:
        re.match(pattern, message.text)
        await message.answer("Quduq chuqurligini kiriting")
    except:
        await message.reply("Quduq raqmini Namunaga binaon to'ldiring❗\n\n"
                            "<b>N A M U N A:</b><code>12345</code>")

