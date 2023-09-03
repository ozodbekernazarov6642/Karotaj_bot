from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

preparation_time = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Tayyor", callback_data="Tayyor"),
            InlineKeyboardButton(text="3 soat", callback_data="3 soat"),
        ],
        [
            InlineKeyboardButton(text="5 soat", callback_data="5 soat"),
            InlineKeyboardButton(text="10 soat", callback_data="10 soat"),
        ],
    ]
)
