from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

preparation_time_ru = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Готовый", callback_data="Готовый"),
            InlineKeyboardButton(text="3 час", callback_data="3 час"),
        ],
        [
            InlineKeyboardButton(text="5 час", callback_data="5 час"),
            InlineKeyboardButton(text="10 час", callback_data="10 час"),
        ],
    ]
)
