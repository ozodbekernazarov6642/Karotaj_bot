from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu_region_uz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='"Uzbek geologiya qidiruv" AJ', callback_data="region_uz:Uz")
        ],
        [
            InlineKeyboardButton(text='"Ozarbayjon" IIChB', callback_data="region_uz:Oz")
        ],
        [
            InlineKeyboardButton(text='"Suv tarraqiyoti" MChJ', callback_data="region_uz:St")
        ],
        [
            InlineKeyboardButton(text='"Samgeoltexservis" MChJ', callback_data="region_uz:Sam")
        ],
        [
            InlineKeyboardButton(text='"Regionalgeologiya" DUK', callback_data="region_uz:Reg")
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data="region_uz:back")
        ]
    ]
)
