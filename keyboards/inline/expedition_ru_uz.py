from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu_expedition_ru_uz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='"Зарафшон" ДГҚЭ', callback_data='expedition_ru:"Зарафшон" ДГҚЭ')
        ],
        [
            InlineKeyboardButton(text='"Шимолий Нурота" ДГҚЭ', callback_data='expedition_ru:"Шимолий Нурота" ДГҚЭ')
        ],
        [
            InlineKeyboardButton(text='"Зармитан" ДГҚЭ', callback_data='expedition_ru:"Зармитан" ДГҚЭ')
        ],
        [
            InlineKeyboardButton(text='"Хисор" ДГҚЭ', callback_data='expedition_ru:"Хисор" ДГҚЭ')
        ],
        [
            InlineKeyboardButton(text='"Сурхон " ДГҚЭ', callback_data='expedition_ru:"Сурхон " ДГҚЭ')
        ],
        [
            InlineKeyboardButton(text='"Кокпатас" ДГҚЭ', callback_data='expedition_ru:"Кокпатас" ДГҚЭ')
        ],
        [
            InlineKeyboardButton(text='"Даугизтау" ДГҚЭ', callback_data='expedition_ru:"Даугизтау" ДГҚЭ')
        ],

        [
            InlineKeyboardButton(text="⬅️ Назад", callback_data='expedition_ru:back"')
        ]
    ]
)
