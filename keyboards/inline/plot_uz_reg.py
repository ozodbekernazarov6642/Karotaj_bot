from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu_plot_uz_muz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Auminzatau GTP (K)", callback_data="plot_uz:AumK"),
            InlineKeyboardButton(text="Auminzatau GTP (Sh)", callback_data="plot_uz:Aum")
        ],
        [
            InlineKeyboardButton(text="Tamditau GTP (K)", callback_data="plot_uz:TamK"),
            InlineKeyboardButton(text="Tamditau GTP (Sh)", callback_data="plot_uz:Tam")
        ],
        [
            InlineKeyboardButton(text="Aristantov GTP (K)", callback_data="plot_uz:ArisK"),
            InlineKeyboardButton(text="Aristantov GTP (Sh)", callback_data="plot_uz:Aris")
        ],
        [
            InlineKeyboardButton(text="Irlir", callback_data="plot_uz:Irlir"),
            InlineKeyboardButton(text="Novkat", callback_data="plot_uz:Irlir")
        ],
        [
            InlineKeyboardButton(text="Ulkentau", callback_data="plot_uz:Ul")
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data="plot_uz_reg:back")
        ]
    ]
)

menu_plot_uz_qor = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Tas-Kazgan", callback_data="plot_uz:Tas")
        ],
        [
            InlineKeyboardButton(text="Quljiqtau", callback_data="plot_uz:Qul")
        ],
        [
            InlineKeyboardButton(text="Sulton Uvays", callback_data="plot_uz:Sul")
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data="plot_uz_reg:back")
        ]
    ]
)

