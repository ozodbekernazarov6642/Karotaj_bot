from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

confirmation = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Tasdiqlash", callback_data="confirmation"),
        ]
    ]
)
