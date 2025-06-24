from models.student import Student
from dao.student_dao import StudentDAO
from models.subject import Subject
from dao.subject_dao import Subject_DAO

class StudentController:
    def registerStudent(self, name, cpf, adress, phone_number, student_id, subject):
        students_txt = StudentDAO.read()
        subjects_txt = Subject_DAO.read()

        is_exists_student = any(student.name == name for student in students_txt)
        is_exists_subject = any(subject.name == subject for subject in subjects_txt)

        if not is_exists_subject and not is_exists_student:
            StudentDAO.save(Student(name, cpf, adress, phone_number, student_id),Subject(subject))
        else:
            return False