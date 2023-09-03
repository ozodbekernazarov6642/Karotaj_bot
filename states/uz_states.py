from aiogram.dispatcher.filters.state import State, StatesGroup


class menu_uz(StatesGroup):
    ru_lang = State()
    uz_lang = State()
    region = State()
    expedition = State()
    plot = State()
    well_number = State()
    depth = State()
    method = State()
    arrival_time = State()
    customer_name = State()
    position = State()
    state_number = State()
    drill_type = State()
    preparation_time = State()
    confirmation = State()
