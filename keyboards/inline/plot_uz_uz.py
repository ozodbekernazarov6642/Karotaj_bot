from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menu_plot_uz_zarafshon = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Salin", callback_data="plot_uz:Salin"),
            InlineKeyboardButton(text="Tashkan", callback_data="plot_uz:Tashkan")
        ],
        [
            InlineKeyboardButton(text="Yangi Davon (metro)", callback_data="plot_uz:YanDavMetro")
        ],
        [
            InlineKeyboardButton(text="Radjan (shimoliy)", callback_data="plot_uz:Radjan")
        ],
        [
            InlineKeyboardButton(text="Yangi Davon (markaziy)", callback_data="plot_uz:YanDavMar")
        ],
        [
            InlineKeyboardButton(text="Yangi Umid", callback_data="plot_uz:Salin"),
            InlineKeyboardButton(text="Yangi Davon", callback_data="plot_uz:YangDav")
        ],
        [
            InlineKeyboardButton(text="Avliyo", callback_data="plot_uz:Avliyo"),
            InlineKeyboardButton(text="Garbiy", callback_data="plot_uz:Garbiy")
        ],
        [
            InlineKeyboardButton(text="Gumsay", callback_data="plot_uz:Gumsay"),
            InlineKeyboardButton(text="Kuchumsay", callback_data="plot_uz:Kuch")
        ],
        [
            InlineKeyboardButton(text="Lapak", callback_data="plot_uz:Lapak"),
            InlineKeyboardButton(text="Ingichka", callback_data="plot_uz:Ing")
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data="plot_uz_uz:back")
        ]
    ]
)

menu_plot_uz_shim = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Oltin Diyor", callback_data="plot_uz:Oltin")
        ],
        [
            InlineKeyboardButton(text="Pistali", callback_data="plot_uz:Pis")
        ],
        [
            InlineKeyboardButton(text="Garbiy Pistali", callback_data="plot_uz:Gap")
        ],
        [
            InlineKeyboardButton(text="Garbiy Kosonsoy", callback_data="plot_uz:Gak")
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data="plot_uz_uz:back")
        ]
    ]
)

menu_plot_uz_zarmitan = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Zarmitan", callback_data="plot_uz:Zarmitan")
        ],
        [
            InlineKeyboardButton(text="Markaziy", callback_data="plot_uz:Markaziy")
        ],
        [
            InlineKeyboardButton(text="Yuqori Saroy", callback_data="plot_uz:Saroy")
        ],
        [
            InlineKeyboardButton(text="Bayram", callback_data="plot_uz:Bayram")
        ],
        [
            InlineKeyboardButton(text="Davlatxoja", callback_data="plot_uz:Dav")
        ],
        [
            InlineKeyboardButton(text="Tukman", callback_data="plot_uz:Tuk")
        ],
        [
            InlineKeyboardButton(text="Ortaliq", callback_data="plot_uz:Or")
        ],
        [
            InlineKeyboardButton(text="Gujumsoy", callback_data="plot_uz:Guj")
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data="plot_uz_uz:back")
        ]
    ]
)

menu_plot_uz_hisor = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Sulatsoy", callback_data="plot_uz:Sulatsoy")
        ],
        [
            InlineKeyboardButton(text="Xodjadiq", callback_data="plot_uz:Xodjadiq")
        ],
        [
            InlineKeyboardButton(text="Kamangaron", callback_data="plot_uz:Kam")
        ],
        [
            InlineKeyboardButton(text="Yaxton", callback_data="plot_uz:Yax")
        ],
        [
            InlineKeyboardButton(text="Iral", callback_data="plot_uz:Iral")
        ],
        [
            InlineKeyboardButton(text="Akba", callback_data="plot_uz:Akba")
        ],
        [
            InlineKeyboardButton(text="Sarikul", callback_data="plot_uz:Sarik")
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data="plot_uz_uz:back")
        ]
    ]
)

menu_plot_uz_surxon = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Maydansan", callback_data="plot_uz:May")
        ],
        [
            InlineKeyboardButton(text="Nilu", callback_data="plot_uz:Nilu")
        ],
        [
            InlineKeyboardButton(text="Shimoliy", callback_data="plot_uz:Shim")
        ],
        [
            InlineKeyboardButton(text="Shimoliy Chinorsoy", callback_data="plot_uz:Chinorsoy")
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data="plot_uz_uz:back")
        ]
    ]
)
menu_plot_uz_kuk = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Chalcharatau (K)", callback_data="plot_uz:ChK"),
            InlineKeyboardButton(text="Chalcharatau (Sh)", callback_data="plot_uz:ChSh")
        ],
        [
            InlineKeyboardButton(text="Saridjoy (K)", callback_data="plot_uz:SK"),
            InlineKeyboardButton(text="Saridjoy (Sh)", callback_data="plot_uz:SSh")
        ],
        [
            InlineKeyboardButton(text="Mingboy (K)", callback_data="plot_uz:MK"),
            InlineKeyboardButton(text="Mingboy (Sh)", callback_data="plot_uz:MSh")
        ],
        [
            InlineKeyboardButton(text="Derbez (K)", callback_data="plot_uz:DK"),
            InlineKeyboardButton(text="Derbez (Sh)", callback_data="plot_uz:DK")
        ],
        [
            InlineKeyboardButton(text="Jetimtau (K)", callback_data="plot_uz:JK"),
            InlineKeyboardButton(text="Jetimtau (Sh)", callback_data="plot_uz:JSh")
        ],
        [
            InlineKeyboardButton(text="⬅️ Ortga", callback_data="plot_uz_uz:back")
        ]
    ]
)
