from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu_expedition_uz_uz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='"Zarafshon" DGQE', callback_data="expedition_uz:Zarafshon")
        ],
        [
            InlineKeyboardButton(text='"Shimoliy Nurota" DGQE', callback_data="expedition_uz:Shim")
        ],
        [
            InlineKeyboardButton(text='"Zarmitan" DGQE', callback_data="expedition_uz:Zarmitan")
        ],
        [
            InlineKeyboardButton(text='"Hisor" DGQE', callback_data="expedition_uz:Hisor")
        ],
        [
            InlineKeyboardButton(text='"Surxon" DGQE', callback_data="expedition_uz:Surxon")
        ],
        [
            InlineKeyboardButton(text='"Kukpatas" DGQE', callback_data="expedition_uz:Kuk")
        ],
        [
            InlineKeyboardButton(text='"Daugiztau" DGQE', callback_data="expedition_uz:Da")
        ],

        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data="expedition_uz:back")
        ]
    ]
)
