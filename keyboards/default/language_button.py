from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menu_lang = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇺🇿 O'zbekcha"),
            KeyboardButton(text="🇷🇺 Руский")
        ]
    ],resize_keyboard=True
)