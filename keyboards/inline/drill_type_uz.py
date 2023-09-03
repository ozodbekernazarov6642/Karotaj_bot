from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

drill_type = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="K", callback_data="K"),
            InlineKeyboardButton(text="Sh", callback_data="Sh"),
        ]
    ]
)
