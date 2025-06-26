from models.models import engine, Student, Teacher, Grade, Subject
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

class ControllerStudent:
    def registerStudent(nameRegister,cpfRegister,adressRegister,phone_numberRegister):

        student = Student(name = nameRegister,
                          cpf = cpfRegister,
                          adress = adressRegister,
                          phone_number = phone_numberRegister)
        
        session.add(student)

class ControllerTeacher:
    def registerTeacher(nameRegister,cpfRegister,adressRegister,phone_numberRegister):
        
        teacher = Teacher(name = nameRegister,
                          cpf = cpfRegister,
                          adress = adressRegister,
                          phone_number = phone_numberRegister)
        
        session.add(teacher)

class ControllerSubject:
    def registerSubject(nameRegister,teacher_id_Register):

        subject = Subject(name = nameRegister,
                          teacher_id = teacher_id_Register)
        
        session.add(subject)

class ControllerGrade:
    def registerGrade(student_id_Register,subject_id_Register,subject_grade_Register):

        grade = Grade(student_id = student_id_Register,
                      subject_id = subject_id_Register,
                      subject_grade = subject_grade_Register)
        
        session.add(grade)

session.commit()