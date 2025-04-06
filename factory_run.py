from factory.coursesFactory import create_course
from factory.teachersFactory import create_teacher
from factory.CourseTeacherFactory import create_CourseTeacher
from factory.loginFactory import create_logins

create_teacher(10)
create_course(5)
create_CourseTeacher(10)
create_logins()