from aiogram.fsm.state import State, StatesGroup

class RegisterState(StatesGroup):
    main = State()
    getFullName = State()
    getAge = State()
    getPhoneNumber = State()