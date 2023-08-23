from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menu_send_button_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✍🏻 Buyurtma berish"),
            KeyboardButton(text="✅ Buyurtma xolatini tekshirish")
        ],
        [
            KeyboardButton(text="📝 Murojaat yuborish")
        ],
        [
            KeyboardButton(text="⬅️ Ortga")
        ]
    ],resize_keyboard=True, one_time_keyboard=True
)