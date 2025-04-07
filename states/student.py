from aiogram.fsm.state import StatesGroup, State

class StudentMain(StatesGroup):
    main = State()

class StudentGroups(StatesGroup):
    main = State()

class NotificationState(StatesGroup):
    main = State()

class StudentPaymenState(StatesGroup):
    main = State()