from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

method_uz = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Gamma Karotaj (GK)", callback_data="Gamma Karotaj (GK)"),
            InlineKeyboardButton(text="Inklnometriya (Ink)", callback_data="Inklnometriya (Ink)"),
        ],
        [
            InlineKeyboardButton(text="KC", callback_data="KC"),
            InlineKeyboardButton(text="Tabiiy elektr maydonlar (ПС)", callback_data="Tabiiy elektr maydonlar (ПС)"),
        ],
        [
            InlineKeyboardButton(text="Kavornometriya (KV)", callback_data="Kavornometriya (KV)"),
            InlineKeyboardButton(text="MAgnit karotaj (KVM)", callback_data="Magnit karotaj (KVM)"),
        ],
    ]
)
