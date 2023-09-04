from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

confirmation_ru = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ Подтверждение", callback_data="confirmation"),
        ]
    ]
)
