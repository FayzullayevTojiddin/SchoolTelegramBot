
from models.group import Group

def get_homeworks_list(group_id):
    homeWorks = Group.getHomeWorks(group_id)
    
    pass