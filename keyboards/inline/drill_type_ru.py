from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

drill_type_ru = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="K", callback_data="K"),
            InlineKeyboardButton(text="Ш", callback_data="Ш"),
        ]
    ]
)
