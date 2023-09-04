from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

method_ru = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Гамма каротаж - ГК", callback_data="Гамма каротаж - ГК"),
            InlineKeyboardButton(text="'Инклинометрия - Инк", callback_data="'Инклинометрия - Инк"),
        ],
        [
            InlineKeyboardButton(text="Каротаж сопротивления - КС", callback_data="Каротаж сопротивления - КС"),
            InlineKeyboardButton(text="Естественный потенциал - ПС", callback_data="Естественный потенциал - ПС"),
        ],
        [
            InlineKeyboardButton(text="'Кавернометрия - КВ", callback_data="'Кавернометрия - КВ"),
            InlineKeyboardButton(text="Магнитный каротаж - КМВ", callback_data="Магнитный каротаж - КМВ"),
        ],
    ]
)
