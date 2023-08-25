from aiogram.dispatcher.filters import Text
from aiogram.types import CallbackQuery
from aiogram import types
import re
from loader import dp
from states.lang_state import Lang_state


@dp.callback_query_handler(Text(startswith='plot_uz'), state=Lang_state.uzb)
async def well_number_uz(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(f"Quduq raqamini kiriting 👇")


@dp.message_handler(Text(startswith="Quduq raqmini"), state=Lang_state.uzb)
async def well_number_uz_check(message: types.Message):
    pattern = r"^[1-9]\d{4}$"
    try:
        re.match(pattern, message.text)
        await message.answer("Quduq chuqurligini kiriting")
    except:
        await message.reply("Quduq raqmini Namunaga binaon to'ldiring❗\n\n"
                            "<b>N A M U N A:</b><code>12345</code>")

