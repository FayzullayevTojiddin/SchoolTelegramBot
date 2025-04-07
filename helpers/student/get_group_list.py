from models.user import User

def get_groups(user_id):
    user = User.get_or_none(user_id)
    if user:
        return user.groups
    else:
        return False