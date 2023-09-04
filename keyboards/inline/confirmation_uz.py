from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

confirmation_uz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅ Tasdiqlash", callback_data="confirmation"),
        ]
    ]
)
