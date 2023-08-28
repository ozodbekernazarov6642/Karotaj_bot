from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

menu_plot_uz_muz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Auminzatau GTP (K)", callback_data="plot_uz:Auminzatau GTP (K)"),
            InlineKeyboardButton(text="Auminzatau GTP (Sh)", callback_data="plot_uz:Auminzatau GTP (Sh)")
        ],
        [
            InlineKeyboardButton(text="Tamditau GTP (K)", callback_data="plot_uz:Tamditau GTP (K)"),
            InlineKeyboardButton(text="Tamditau GTP (Sh)", callback_data="plot_uz:Tamditau GTP (Sh)")
        ],
        [
            InlineKeyboardButton(text="Aristantov GTP (K)", callback_data="plot_uz:Aristantov GTP (K)"),
            InlineKeyboardButton(text="Aristantov GTP (Sh)", callback_data="plot_uz:Aristantov GTP (Sh)")
        ],
        [
            InlineKeyboardButton(text="Irlir", callback_data="plot_uz:Irlir"),
            InlineKeyboardButton(text="Novkat", callback_data="plot_uz:Novkat")
        ],
        [
            InlineKeyboardButton(text="Ulkentau", callback_data="plot_uz:Ulkentau")
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data="plot_uz_reg:back")
        ]
    ]
)

menu_plot_uz_qor = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Tas-Kazgan", callback_data="plot_uz:Tas-Kazgan")
        ],
        [
            InlineKeyboardButton(text="Quljiqtau", callback_data="plot_uz:Quljiqtau")
        ],
        [
            InlineKeyboardButton(text="Sulton Uvays", callback_data="plot_uz:Sulton Uvays")
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data="plot_uz_reg:back")
        ]
    ]
)

