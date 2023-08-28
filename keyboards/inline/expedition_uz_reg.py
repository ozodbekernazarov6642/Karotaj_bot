from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu_expedition_uz_reg = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='"Markaziy Uzbeksitan" DGTE', callback_data='expedition_uz:"Markaziy '
                                                                                  'Uzbeksitan" DGTE')
        ],
        [
            InlineKeyboardButton(text='"Qoraqalpoq" DGTE', callback_data='expedition_uz:"Qoraqalpoq" DGTE')
        ],
        [
            InlineKeyboardButton(text='"Sharqiy Uzbekistan" DGTE', callback_data='expedition_uz:"Sharqiy Uzbekistan" '
                                                                                 'DGTE')
        ],
        [
            InlineKeyboardButton(text='"Markaziy" GGE', callback_data='expedition_uz:"Markaziy" GGE')
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data="expedition_uz:back")
        ]
    ]
)