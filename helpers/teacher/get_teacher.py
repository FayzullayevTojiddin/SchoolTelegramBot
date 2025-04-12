
from models.group import Group

def get_teacher_id_by_group_id(group_id):
    group = Group.get_by_id(group_id)
    return group.teacher_id