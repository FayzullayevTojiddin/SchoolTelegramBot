
from models.group import Group
from models.homework import HomeWork

from helpers.student.get_homeworks import (
    getHomeWorkListTextHelper, getHomeWorkDetailTextHelper
)

from keyboards.index_keyboars import homeWorkListKeyboard
from keyboards.about_keyboards import get_about_homework_keyboard

def get_homeworks_list(group_id):
    homeWorks = Group.getHomeWorks(group_id)
    text = getHomeWorkListTextHelper(len(homeWorks), group_id)
    keyboard = homeWorkListKeyboard(homeWorks, group_id)
    state = None
    return text, keyboard, state

def get_homework(homework_id, group_id):
    homework = HomeWork.get_by_id(homework_id)
    text = getHomeWorkDetailTextHelper(homework)
    keyboard = get_about_homework_keyboard(group_id)
    state = None
    
    return text, keyboard, state