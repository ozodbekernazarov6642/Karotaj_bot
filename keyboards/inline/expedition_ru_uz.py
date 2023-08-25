from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu_expedition_ru_uz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='"Зарафшон" ДГҚЭ', callback_data="expedition_ru:Zarafshon")
        ],
        [
            InlineKeyboardButton(text='"Шимолий Нурота" ДГҚЭ', callback_data="expedition_ru:Shim")
        ],
        [
            InlineKeyboardButton(text='"Зармитан" ДГҚЭ', callback_data="expedition_ru:Zarmitan")
        ],
        [
            InlineKeyboardButton(text='"Хисор" ДГҚЭ', callback_data="expedition_ru:Hisor")
        ],
        [
            InlineKeyboardButton(text='"Сурхон " ДГҚЭ', callback_data="expedition_ru:Surxon")
        ],
        [
            InlineKeyboardButton(text='"Кокпатас" ДГҚЭ', callback_data="expedition_ru:Kuk")
        ],
        [
            InlineKeyboardButton(text='"Даугизтау" ДГҚЭ', callback_data="expedition_ru:Da")
        ],

        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data="expedition_ru:back")
        ]
    ]
)
