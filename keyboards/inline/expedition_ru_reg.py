from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu_expedition_ru_reg = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='"Марказий-Ўзбекистон" ДГТЭ',
                                 callback_data='expedition_ru:"Марказий-Ўзбекистон" ДГТЭ')
        ],
        [
            InlineKeyboardButton(text='"Қорақалпоқ" ДГТЭ', callback_data='expedition_ru:"Қорақалпоқ" ДГТЭ')
        ],
        [
            InlineKeyboardButton(text='"Шарқий-Ўзбекистон" ДГТЭ',
                                 callback_data='expedition_ru:"Шарқий-Ўзбекистон" ДГТЭ')
        ],
        [
            InlineKeyboardButton(text='"Марказий" ГГЭ', callback_data='expedition_ru:"Марказий" ГГЭ')
        ],
        [
            InlineKeyboardButton(text="⬅️ Назад", callback_data="expedition_ru:back")
        ]
    ]
)
