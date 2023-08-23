from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu_region_uz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📍Andijon viloyati", callback_data="region_uz:An"),
            InlineKeyboardButton(text="📍Buxoro viloyati", callback_data="region_uz:Bu"),
        ],
        [
            InlineKeyboardButton(text="📍Farg'ona viloyati", callback_data="region_uz:Fa"),
            InlineKeyboardButton(text="📍Jizzax viloyati", callback_data="region_uz:Ji"),
        ],
        [
            InlineKeyboardButton(text="📍Namangan viloyati", callback_data="region_uz:Nam"),
            InlineKeyboardButton(text="📍Qashqadaryo viloyati", callback_data="region_uz:Qa"),
        ],
        [
            InlineKeyboardButton(text="📍Navoiy viloyati", callback_data="region_uz:Nav"),
            InlineKeyboardButton(text="📍Qoraqolpo'iston Respublikasi", callback_data="region_uz:Qo"),
        ],
        [
            InlineKeyboardButton(text="📍Samarqand viloyati", callback_data="region_uz:Sa"),
            InlineKeyboardButton(text="📍Sirdaryo viloyati", callback_data="region_uz:Si"),
        ],
        [
            InlineKeyboardButton(text="📍Surxondaryo viloyati", callback_data="region_uz:Su"),
            InlineKeyboardButton(text="📍Toshkent viloyati", callback_data="region_uz:Tov"),
        ],
        [
            InlineKeyboardButton(text="📍Toshkent shahri", callback_data="region_uz:Tos"),
            InlineKeyboardButton(text="📍Xorazm viloyati", callback_data="region_uz:Xo"),
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data="region_uz:back")
        ]
    ]
)