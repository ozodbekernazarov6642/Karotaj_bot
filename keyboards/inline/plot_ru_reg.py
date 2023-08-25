from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu_plot_ru_muz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ауминзатау ГТП (к)", callback_data="plot_ru:AumK"),
            InlineKeyboardButton(text="Ауминзатау ГТП (ш)", callback_data="plot_ru:Aum")
        ],
        [
            InlineKeyboardButton(text="Тамдитау ГТП (к)", callback_data="plot_ru:TamK"),
            InlineKeyboardButton(text="Тамдитау ГТП (ш)", callback_data="plot_ru:Tam")
        ],
        [
            InlineKeyboardButton(text="Аристантов ГТП (к)", callback_data="plot_ru:ArisK"),
            InlineKeyboardButton(text="Аристантов ГТП (ш)", callback_data="plot_ru:Aris")
        ],
        [
            InlineKeyboardButton(text="Ирлир", callback_data="plot_ru:Irlir"),
            InlineKeyboardButton(text="Новкат", callback_data="plot_ru:Irlir")
        ],
        [
            InlineKeyboardButton(text="Улкентау", callback_data="plot_ru:Ul")
        ],
        [
            InlineKeyboardButton(text="⬅️ Назад", callback_data="plot_ru_reg:back")
        ]
    ]
)

menu_plot_ru_qor = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Тас-Казган", callback_data="plot_ru:Tas")
        ],
        [
            InlineKeyboardButton(text="Кульджуктау", callback_data="plot_ru:Qul")
        ],
        [
            InlineKeyboardButton(text="Султанувайс (съёмка)", callback_data="plot_ru:Sul")
        ],
        [
            InlineKeyboardButton(text="⬅️ Назад", callback_data="plot_ru_reg:back")
        ]
    ]
)

