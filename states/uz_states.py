from aiogram.dispatcher.filters.state import State, StatesGroup

class menu_uz(StatesGroup):
    uz_lang = State()
    region = State()
    expedition = State()
    plot = State()
    well_number = State()
    depth = State()
    method = State()
    arrival_time = State()
    customer_name = State()
    
