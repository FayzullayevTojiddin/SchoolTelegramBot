from factory.coursesFactory import create_course
from factory.teachersFactory import create_teacher
from factory.studentFactory import create_student
from factory.CourseTeacherFactory import create_CourseTeacher
from factory.loginFactory import create_logins
from factory.notifictionFactory import create_notification
from factory.groupFactory import create_group
from factory.groupStudentFactory import create_groupStudent
from factory.paymentStudentFactory import create_studentPayment

create_logins()
create_student(100)
create_teacher(10)
create_course(5)
create_group(10)
create_notification(5)
create_CourseTeacher(10)
create_groupStudent(5)
create_studentPayment(5)