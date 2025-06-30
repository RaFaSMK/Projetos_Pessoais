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

    def listAll():
        studentList = session.query(Student).all()
        result = []

        for i in studentList:
            result.append(f"ID: '{i.id}'", f"Name: '{i.name}'", f"CPF: '{i.cpf}'", f"Adress: '{i.adress}'", f"Phone Number: '{i.phone_number}'","\n")

        return result
    
    def idSearch(student_id):

        student = session.query(Student).filter(Student(id) == student_id).all()

        for i in student:
            return f"ID: '{i.id}'", f"Name: '{i.name}'", f"CPF: '{i.cpf}'", f"Adress: '{i.adress}'", f"Phone Number: '{i.phone_number}'","\n"

class ControllerTeacher:
    def registerTeacher(nameRegister,cpfRegister,adressRegister,phone_numberRegister):
        
        teacher = Teacher(name = nameRegister,
                          cpf = cpfRegister,
                          adress = adressRegister,
                          phone_number = phone_numberRegister)
        
        session.add(teacher)

    def listAll():

        teacherList = session.query(Teacher).all()
        result = []

        for i in teacherList:
            result.append(f"ID: '{i.id}'", f"Name: '{i.name}'", f"CPF: '{i.cpf}'", f"Adress: '{i.adress}'", f"Phone Number: '{i.phone_number}'","\n")

        return result

class ControllerSubject:
    def registerSubject(nameRegister,):

        subject = Subject(name = nameRegister)
        session.add(subject)
    
    def associateTeacher(teacher_id_Associate):

        teacher_associate = Subject(teacher_id = teacher_id_Associate)
        session.add(teacher_associate)

    def associateStudent(student_id_Associate):

        student_associate = Subject(student_id = student_id_Associate)
        session.add(student_associate)

    def listAll():

        subjectList = session.query(Subject).all()
        result = []

        for i in subjectList:
            result.append(f"ID: '{i.id}'", f"Name: '{i.name}'", f"Teacher_id: '{i.teacher_id}'", f"Student_id '{i.student_id}'\n")

        return result

class ControllerGrade:
    def registerGrade(student_id_Register,subject_id_Register,subject_grade_1_sem_Register,subject_grade_2_sem_Register):

        grade = Grade(student_id = student_id_Register,
                      subject_id = subject_id_Register,
                      subject_grade_1_sem = subject_grade_1_sem_Register,
                      subject_grade_2_sem = subject_grade_2_sem_Register)
    
        session.add(grade)

    def alterGrade(grade_id, student_id_alter, subject_grade_1_sem_alter, subject_grade_2_sem_alter):

        alter = session.query(Grade).filter(Grade(id) == grade_id).all()

        alter[0].student_id = student_id_alter
        alter[0].subject_grade_1_sem = subject_grade_1_sem_alter
        alter[0].subject_grade_2_sem = subject_grade_2_sem_alter

    def calculateAverage(grade_id_avg):

        grade_1_sem_Avg = session.query(Grade).filter(Grade(id) == grade_id_avg).filter(Grade(grade_1_sem_Avg)).first()
        grade_2_sem_Avg = session.query(Grade).filter(Grade(id) == grade_id_avg).filter(Grade(grade_2_sem_Avg)).first()

        avg = grade_1_sem_Avg.subject_grade_1_sem + grade_2_sem_Avg.id ## Revisar

        return avg
    
    def listAll():
        pass

session.commit()