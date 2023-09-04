from aiogram.dispatcher.filters import Text
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram import types
import re
from loader import dp
from states.ru_states import menu_ru
from utils.list.app_list import app_list
from keyboards.default.menu_button import menu_back


@dp.callback_query_handler(text="plot_ru:Салин", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Ташкан", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Янги Давон (подземка)", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Раджан (Северный)", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Янги Давон (Марказий)", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Янги Умид", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Янги Давон", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Авлиё", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Ғарбий", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Гумсай", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Кучумсай", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Лапак", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Ингичка", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Олтин Диёр", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Пистали", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Ғарбий Пистали", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Ғарбий Косонсой", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Зармитан", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Центральный", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Юкори Сарой", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Байрам", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Давлатхўжа", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Тукман", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Ўрталик", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Ғужумсой", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Сулатсой", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Ходжадык (поверх.)", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Камангорон", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Яхтон", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Ирал", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Акба", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Сарыкуль", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Майдансай", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Нилу", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Северный", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Северный Чинорсой", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Чалчаратау (к)", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Чалчаратау (ш)", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Сарыджой (к)", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Сарыджой (ш)", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Мингбой (к)", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Мингбой (ш)", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Дербез (к)", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Дербез (ш)", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Джетимтау (к)", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Джетимтау (ш)", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Ауминзатау ГТП (к)", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Ауминзатау ГТП (ш)", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Тамдитау ГТП (к)", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Тамдитау ГТП (ш)", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Аристантов ГТП (к)", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Аристантов ГТП (ш)", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Ирлир", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Новкат", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Улкентау", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Тас-Казган", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Кульджуктау", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()


@dp.callback_query_handler(text="plot_ru:Султанувайс (съёмка)", state=menu_ru.plot)
async def well_number_uz(call: CallbackQuery, state: FSMContext):
    plot = call.data.split(":")[1]
    app_list["plot"] = plot
    await call.message.delete()
    await call.message.answer("Введите номер скважины", reply_markup=menu_back)
    await menu_ru.next()
