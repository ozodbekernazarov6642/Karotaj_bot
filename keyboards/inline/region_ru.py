from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu_region_ru = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='АО "Ўзбек геология қидирув"',
                                 callback_data='region_ru:АО "Ўзбек геология қидирув"')
        ],
        [
            InlineKeyboardButton(text='НПО "Азербайджан"', callback_data='region_ru:НПО "Азербайджан"')
        ],
        [
            InlineKeyboardButton(text='СП "Сув тараққиёти"', callback_data='region_ru:СП "Сув тараққиёти"')
        ],
        [
            InlineKeyboardButton(text='ООО "Самгеолтехсервис"', callback_data='region_ru:ООО "Самгеолтехсервис"')
        ],
        [
            InlineKeyboardButton(text='"Регионалгеология" ДМ', callback_data='region_ru:"Регионалгеология" ДМ')
        ],
        [
            InlineKeyboardButton(text="⬅️ Назад", callback_data="region_ru:back")
        ]
    ]
)
