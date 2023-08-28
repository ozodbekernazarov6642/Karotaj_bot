from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from states.uz_states import menu_uz
from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")
    
    await message.answer("\n".join(text))


@dp.message_handler(CommandHelp(), state=menu_uz.uz_lang)
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")

    await message.answer("\n".join(text))


@dp.message_handler(CommandHelp(), state=menu_uz.uz_lang)
async def bot_help(message: types.Message):
    text = ("Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam")

    await message.answer("\n".join(text))
