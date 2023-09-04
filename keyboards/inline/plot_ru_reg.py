from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu_plot_ru_muz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ауминзатау ГТП (к)", callback_data="plot_ru:Ауминзатау ГТП (к)"),
            InlineKeyboardButton(text="Ауминзатау ГТП (ш)", callback_data="plot_ru:Ауминзатау ГТП (ш)")
        ],
        [
            InlineKeyboardButton(text="Тамдитау ГТП (к)", callback_data="plot_ru:Тамдитау ГТП (к)"),
            InlineKeyboardButton(text="Тамдитау ГТП (ш)", callback_data="plot_ru:Тамдитау ГТП (ш)")
        ],
        [
            InlineKeyboardButton(text="Аристантов ГТП (к)", callback_data="plot_ru:Аристантов ГТП (к)"),
            InlineKeyboardButton(text="Аристантов ГТП (ш)", callback_data="plot_ru:Аристантов ГТП (ш)")
        ],
        [
            InlineKeyboardButton(text="Ирлир", callback_data="plot_ru:Ирлир"),
            InlineKeyboardButton(text="Новкат", callback_data="plot_ru:Новкат")
        ],
        [
            InlineKeyboardButton(text="Улкентау", callback_data="plot_ru:Улкентау")
        ],
        [
            InlineKeyboardButton(text="⬅️ Назад", callback_data="plot_ru_reg:back")
        ]
    ]
)

menu_plot_ru_qor = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Тас-Казган", callback_data="plot_ru:Тас-Казган")
        ],
        [
            InlineKeyboardButton(text="Кульджуктау", callback_data="plot_ru:Кульджуктау")
        ],
        [
            InlineKeyboardButton(text="Султанувайс (съёмка)", callback_data="plot_ru:Султанувайс (съёмка)")
        ],
        [
            InlineKeyboardButton(text="⬅️ Назад", callback_data="plot_ru_reg:back")
        ]
    ]
)

