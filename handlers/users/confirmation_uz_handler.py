import uuid
from uuid import uuid1

from aiogram import types
from aiogram.dispatcher import FSMContext
from utils.time_Tashkent import time
from loader import dp, bot
from states.uz_states import menu_uz
from utils.list.app_list import app_list


@dp.callback_query_handler(text="confirmation", state=menu_uz.confirmation)
async def send_confirmation(call: types.CallbackQuery, state: FSMContext):
    time1 = await time()
    message = (
        f" Buyurtma raqami: {uuid.uuid4()}\n\n"
        f"✅ Buyurtma berilgan vaqt:{time1}\n\n"
        f"🔰 Korxona nomi: {app_list.get('region')}\n\n"
        f"🔍 Ekspeditsiya nomi: {app_list.get('expedition')}\n\n"
        f"📍 Uchastka nomi: {app_list.get('plot')}\n\n"
        f"⛏️ Quduq raqami: {app_list.get('well_number')}\n\n"
        f"📏 Quduq chuqurligi: {app_list.get('depth')}\n\n"
        f"📝 Metod: {app_list.get('method')}\n\n"
        f"🚚 Yetib borish sanasi: {app_list.get('arrival_time')}\n\n"
        f"🕵️‍♂️ Buyurtmachi ismi: {app_list.get('customer_name')}\n\n"
        f"🪑 Buyurtmachi lavozimi: {app_list.get('position')}\n\n"
        f"🔢 Davlat raqami: {app_list.get('state_number')}\n\n"
        f"🧨 Burg'u turi: {app_list.get('drill_type')}\n\n"
        f"🕠 Quduq tayyor bo'lish vaqti: {app_list.get('preparation_time')}")
    await bot.send_message(chat_id=2047459736, text=message)
    await call.message.answer("✅ Buyurtma tasdiqlandi!")
    await call.message.delete()
    await state.finish()
