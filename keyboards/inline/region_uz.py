from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu_region_uz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='"O\'zbek geologiya qidiruv" AJ', callback_data='region_uz:"O\'zbek geologiya '
                                                                                      'qidiruv" AJ')
        ],
        [
            InlineKeyboardButton(text='"Ozarbayjon" IIChB', callback_data='region_uz:"Ozarbayjon" IIChB')
        ],
        [
            InlineKeyboardButton(text='"Suv tarraqiyoti" MChJ', callback_data='region_uz:"Suv tarraqiyoti" MChJ')
        ],
        [
            InlineKeyboardButton(text='"Samgeoltexservis" MChJ', callback_data='region_uz:"Samgeoltexservis" MChJ')
        ],
        [
            InlineKeyboardButton(text='"Regionalgeologiya" DUK', callback_data='region_uz:"Regionalgeologiya" DUK')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data="region_uz:back")
        ]
    ]
)
