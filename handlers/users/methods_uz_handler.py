from aiogram import types

from keyboards.inline.expedition_uz_reg import menu_expedition_uz_reg
from keyboards.inline.expedition_uz_uz import menu_expedition_uz_uz
from loader import dp
from states.uz_states import menu_uz
from utils.list.app_list import app_list


@dp.callback_query_handler(text="Gamma Karotaj (GK)", state=menu_uz.method)
async def send_expedition(call: types.CallbackQuery):
    app_list["method"] = call.data
    await call.message.answer("Zond yetib borish vaqtini kiriting (kk/oo/yyyy)")
    await call.message.delete()
    await menu_uz.next()


@dp.callback_query_handler(text="Inklnometriya (Ink)", state=menu_uz.method)
async def send_expedition(call: types.CallbackQuery):
    app_list["method"] = call.data
    await call.message.answer("Zond yetib borish vaqtini kiriting (kk/oo/yyyy)")
    await call.message.delete()
    await menu_uz.next()


@dp.callback_query_handler(text="KC", state=menu_uz.method)
async def send_expedition(call: types.CallbackQuery):
    app_list["method"] = call.data
    await call.message.answer("Zond yetib borish vaqtini kiriting (kk/oo/yyyy)")
    await call.message.delete()
    await menu_uz.next()


@dp.callback_query_handler(text="Tabiiy elektr maydonlar (ПС)", state=menu_uz.method)
async def send_expedition(call: types.CallbackQuery):
    app_list["method"] = call.data
    await call.message.answer("Zond yetib borish vaqtini kiriting (kk/oo/yyyy)")
    await call.message.delete()
    await menu_uz.next()


@dp.callback_query_handler(text="Kavornometriya (KV)", state=menu_uz.method)
async def send_expedition(call: types.CallbackQuery):
    app_list["method"] = call.data
    await call.message.answer("Zond yetib borish vaqtini kiriting (kk/oo/yyyy)")
    await call.message.delete()
    await menu_uz.next()


@dp.callback_query_handler(text="Magnit karotaj (KVM)", state=menu_uz.method)
async def send_expedition(call: types.CallbackQuery):
    app_list["method"] = call.data
    await call.message.answer("Zond yetib borish vaqtini kiriting (kk/oo/yyyy)")
    await call.message.delete()
    await menu_uz.next()
