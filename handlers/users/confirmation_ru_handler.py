import uuid
from uuid import uuid1

from aiogram import types
from aiogram.dispatcher import FSMContext

from states.ru_states import menu_ru
from utils.time_Tashkent import time
from loader import dp, bot
from utils.list.app_list import app_list


@dp.callback_query_handler(text="confirmation", state=menu_ru.confirmation)
async def send_confirmation(call: types.CallbackQuery, state: FSMContext):
    time1 = await time()
    message = (
        f" Номер заказа: {uuid.uuid4()}\n\n"
        f"✅ Время размещения заказа: {time1}\n\n"
        f"🔰 Название компании: {app_list.get('region')}\n\n"
        f"🔍 Название экспедиции: {app_list.get('expedition')}\n\n"
        f"📍 Название участка: {app_list.get('plot')}\n\n"
        f"⛏️ Номер скважины: {app_list.get('well_number')}\n\n"
        f"📏 Глубина скважины: {app_list.get('depth')}\n\n"
        f"📝 Метод: {app_list.get('method')}\n\n"
        f"🚚 Дата прибытия: {app_list.get('arrival_time')}\n\n"
        f"🕵️‍♂️ Имя заказчика: {app_list.get('customer_name')}\n\n"
        f"🪑 Позиция заказчика: {app_list.get('position')}\n\n"
        f"🔢 Государственный номер: {app_list.get('state_number')}\n\n"
        f"🧨 Тип сверла: {app_list.get('drill_type')}\n\n"
        f"🕠 Пора подготовить скважины: {app_list.get('preparation_time')}")
    await bot.send_message(chat_id=2047459736, text=message)
    await call.message.answer("✅ Заказ подтвержден!")
    await call.message.delete()
    await state.finish()
