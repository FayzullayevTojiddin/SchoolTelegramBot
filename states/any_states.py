from aiogram.fsm.state import State, StatesGroup

class MainState(StatesGroup):
    main = State()
    courses = State()

class CourseState(StatesGroup):
    main = State()
    select = State()

class TeacherState(StatesGroup):
    main = State()

class FeedbakState(StatesGroup):
    main = State()

class TeacherState(StatesGroup):
    main = State()