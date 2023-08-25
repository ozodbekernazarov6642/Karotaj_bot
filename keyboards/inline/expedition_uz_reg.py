from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu_expedition_uz_reg = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='"Markaziy Uzbeksitan" DGTE', callback_data="expedition_uz:Muz")
        ],
        [
            InlineKeyboardButton(text='"Qoraqalpoq" DGTE', callback_data="expedition_uz:Qor")
        ],
        [
            InlineKeyboardButton(text='"Sharqiy Uzbekistan" DGTE', callback_data="expedition_uz:Shar")
        ],
        [
            InlineKeyboardButton(text='"Markaziy" GGE', callback_data="expedition_uz:Mar")
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data="expedition_uz:back")
        ]
    ]
)