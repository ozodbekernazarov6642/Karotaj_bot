from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu_region_ru = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='АО "Ўзбек геология қидирув"', callback_data="region_ru:Uz")
        ],
        [
            InlineKeyboardButton(text='НПО "Азербайджан"', callback_data="region_ru:Oz")
        ],
        [
            InlineKeyboardButton(text='СП "Сув тараққиёти"', callback_data="region_ru:St")
        ],
        [
            InlineKeyboardButton(text='ООО "Самгеолтехсервис"', callback_data="region_ru:Sam")
        ],
        [
            InlineKeyboardButton(text='"Регионалгеология" ДМ', callback_data="region_ru:Reg")
        ],
        [
            InlineKeyboardButton(text="⬅️ Назад", callback_data="region_ru:back")
        ]
    ]
)
