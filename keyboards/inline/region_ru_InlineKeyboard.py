from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu_region_ru = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📍Андижанская область", callback_data="region_ru:An"),
            InlineKeyboardButton(text="📍Бухарская область", callback_data="region_ru:Bu"),
        ],
        [
            InlineKeyboardButton(text="📍Ферганская область", callback_data="region_ru:Fa"),
            InlineKeyboardButton(text="📍Джизакская область", callback_data="region_ru:Ji"),
        ],
        [
            InlineKeyboardButton(text="📍Наманганская область", callback_data="region_ru:Nam"),
            InlineKeyboardButton(text="📍Кашкадарьинская область", callback_data="region_ru:Qa"),
        ],
        [
            InlineKeyboardButton(text="📍Навоийская область", callback_data="region_ru:Nav"),
            InlineKeyboardButton(text="📍Республика Каракалпакстан", callback_data="region_ru:Qo"),
        ],
        [
            InlineKeyboardButton(text="📍Самаркандская область", callback_data="region_ru:Sa"),
            InlineKeyboardButton(text="📍Сырдарьинская область", callback_data="region_ru:Si"),
        ],
        [
            InlineKeyboardButton(text="📍Сурхандарьинская область", callback_data="region_ru:Su"),
            InlineKeyboardButton(text="📍Ташкентская область", callback_data="region_ru:Tov"),
        ],
        [
            InlineKeyboardButton(text="📍Город Ташкент", callback_data="region_ru:Tos"),
            InlineKeyboardButton(text="📍Хорезмская область", callback_data="region_ru:Xo"),
        ],
        [
            InlineKeyboardButton(text="⬅️ Назад", callback_data="region_ru:back")
        ]
    ]
)