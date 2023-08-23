from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menu_send_button_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✍🏻 Разместить заказ"),
            KeyboardButton(text="✅ Проверить статус заказа")
        ],
        [
            KeyboardButton(text="📝 Отправить запрос")
        ],
        [
            KeyboardButton(text="⬅️ Назад")
        ]
    ], resize_keyboard=True, one_time_keyboard=True
)