from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu_plot_uz_zarafshon = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Salin", callback_data="plot_uz_Salin"),
            InlineKeyboardButton(text="Tashkan", callback_data="plot_uz_Tashkan")
        ],
        [
            InlineKeyboardButton(text="Yangi Davon (metro)", callback_data="plot_uz_YanDavMetro")
        ],
        [
            InlineKeyboardButton(text="Radjan (shimoliy)", callback_data="Radjan")
        ],
        [
            InlineKeyboardButton(text="Yangi Davon (markaziy)", callback_data="YanDavMar")
        ],
        [
            InlineKeyboardButton(text="Yangi Umid", callback_data="plot_uz_Salin"),
            InlineKeyboardButton(text="Yangi Davon", callback_data="plot_uz_YangDav")
        ],
        [
            InlineKeyboardButton(text="Avliyo", callback_data="plot_uz_Avliyo"),
            InlineKeyboardButton(text="Garbiy", callback_data="plot_uz_Garbiy")
        ],
        [
            InlineKeyboardButton(text="Gumsay", callback_data="plot_uz_Gumsay"),
            InlineKeyboardButton(text="Kuchumsay", callback_data="plot_uz_Kuch")
        ],
        [
            InlineKeyboardButton(text="Lapak", callback_data="plot_uz_Lapak"),
            InlineKeyboardButton(text="Ingichka", callback_data="plot_uz_Ing")
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data="plot_uz:back")
        ]
    ]
)

menu_plot_uz_shim = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Oltin Diyor", callback_data="plot_uz_Oltin")
        ],
        [
            InlineKeyboardButton(text="Pistali", callback_data="plot_uz_Pis")
        ],
        [
            InlineKeyboardButton(text="Garbiy Pistali", callback_data="plot_uz_Gap")
        ],
        [
            InlineKeyboardButton(text="Garbiy Kosonsoy", callback_data="plot_uz_Gak")
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data="plot_uz:back")
        ]
    ]
)
