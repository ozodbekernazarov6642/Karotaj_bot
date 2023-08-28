from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu_expedition_uz_uz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='"Zarafshon" DGQE', callback_data='expedition_uz:"Zarafshon" DGQE')
        ],
        [
            InlineKeyboardButton(text='"Shimoliy Nurota" DGQE', callback_data='expedition_uz:"Shimoliy Nurota" DGQE')
        ],
        [
            InlineKeyboardButton(text='"Zarmitan" DGQE', callback_data='expedition_uz:"Zarmitan" DGQE')
        ],
        [
            InlineKeyboardButton(text='"Hisor" DGQE', callback_data='expedition_uz:"Hisor" DGQE')
        ],
        [
            InlineKeyboardButton(text='"Surxon" DGQE', callback_data='expedition_uz:"Surxon" DGQE')
        ],
        [
            InlineKeyboardButton(text='"Kukpatas" DGQE', callback_data='expedition_uz:"Kukpatas" DGQE')
        ],
        [
            InlineKeyboardButton(text='"Daugiztau" DGQE', callback_data='expedition_uz:"Daugiztau" DGQE')
        ],

        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data="expedition_uz:back")
        ]
    ]
)
