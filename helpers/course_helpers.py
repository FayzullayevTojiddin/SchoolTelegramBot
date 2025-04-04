from models.course import Course

def show_course(course_id):
    try:
        course = Course.get_by_id(course_id)
        
    except:
        pass