from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu_expedition_ru_reg = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='"Марказий-Ўзбекистон" ДГТЭ', callback_data="expedition_ru:Muz")
        ],
        [
            InlineKeyboardButton(text='"Қорақалпоқ" ДГТЭ', callback_data="expedition_ru:Qor")
        ],
        [
            InlineKeyboardButton(text='"Шарқий-Ўзбекистон" ДГТЭ', callback_data="expedition_ru:Shar")
        ],
        [
            InlineKeyboardButton(text='"Марказий" ГГЭ', callback_data="expedition_ru:Mar")
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data="expedition_ru:back")
        ]
    ]
)