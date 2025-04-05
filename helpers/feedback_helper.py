from models.feedback import Feedback

def get_request(request, user_id):
    try:
        return Feedback.create(
            user_id=user_id,
            question=request
        )
    except:
        return False