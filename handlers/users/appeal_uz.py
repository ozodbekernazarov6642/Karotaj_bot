from aiogram import types
from aiogram.dispatcher import FSMContext
from states.lang_state import Lang_state
from states.other_states import Appeal_state
from keyboards.default.lang_uz_button import Leave_information
from loader import dp


@dp.message_handler(text="📝 Murojaat yuborish", state=Lang_state.uzb)
async def appeal_uz(message: types.Message):
    await message.answer("Murojaat qoldirish uchun\n"
                         "Ma'lumotingizni to'ldiring ✍🏻", reply_markup=Leave_information)
    await Appeal_state.appeal_state.set()


