from models.models import engine, Student, Teacher, Grade, Subject
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()


class ControllerStudent:
    @staticmethod # Metodo estático pois não usa o CLS ja que estou usando o BD
    def registerStudent(nameRegister,cpfRegister,adressRegister,phone_numberRegister):

        student = Student(name = nameRegister,
                          cpf = cpfRegister,
                          adress = adressRegister,
                          phone_number = phone_numberRegister)
        
        session.add(student) # Adiciona na camada session o novo valor para ser inserido no BD
        session.commit() # Persiste a session no BD

    @staticmethod
    def listAll():
        studentList = session.query(Student).all() # Retorna uma consulta de todos os valores da classe Student, que é a tabela "student"
        result = [] # Lista para armazenar os valores

        for i in studentList:
            result.append(f"[ID: '{i.id}' Name: '{i.name}' CPF: '{i.cpf}' Adress: '{i.adress}' Phone Number: '{i.phone_number}']") # Insere dentro da lista uma string formatada de cada elemento dentro do studenList

        return "\n".join(result) # O Join concatena os elementos (str) da lista, e a sintaxe é separador.join(o iterável)
    
    @staticmethod
    def idSearch(student_id):

        student = session.query(Student).filter(Student.id == student_id).first() # Agora a consulta tem um filtro pelo ID e retorna somente o primeiro, ja que é por ID, terá somente 1

        return f"[ID: '{student.id}' Name: '{student.name}' CPF: '{student.cpf}' Adress: '{student.adress}' Phone Number: '{student.phone_number}']"

class ControllerTeacher:
    def registerTeacher(nameRegister,cpfRegister,adressRegister,phone_numberRegister):
        
        teacher = Teacher(name = nameRegister,
                          cpf = cpfRegister,
                          adress = adressRegister,
                          phone_number = phone_numberRegister)
        
        session.add(teacher)
        session.commit()

    def listAll():

        teacherList = session.query(Teacher).all()
        result = []

        for i in teacherList:
            result.append(f"[ID: '{i.id}' Name: '{i.name}' CPF: '{i.cpf}' Adress: '{i.adress}' Phone Number: '{i.phone_number}']")

        return "\n".join(result)

class ControllerSubject:
    def registerSubject(nameRegister):

        subject = Subject(name = nameRegister)
        session.add(subject)
        session.commit()
    
    def associateTeacher(teacher_id_Associate):

        teacher_associate = Subject(teacher_id = teacher_id_Associate)
        session.add(teacher_associate)
        session.commit()

    def associateStudent(student_id_Associate):

        student_associate = Subject(student_id = student_id_Associate)
        session.add(student_associate)
        session.commit()

    def listAll():

        subjectList = session.query(Subject).all()
        result = []

        for i in subjectList:
            result.append(f"[ID: '{i.id}' Name: '{i.name}' Teacher_id: '{i.teacher_id}' Student_id: '{i.student_id}']")

        return "\n".join(result)

class ControllerGrade:
    def registerGrade(student_id_Register,subject_id_Register,subject_grade_1_sem_Register,subject_grade_2_sem_Register):

        grade = Grade(student_id = student_id_Register,
                      subject_id = subject_id_Register,
                      subject_grade_1_sem = subject_grade_1_sem_Register,
                      subject_grade_2_sem = subject_grade_2_sem_Register)
    
        session.add(grade)
        session.commit()

    def alterGrade(grade_id, student_id_alter, subject_grade_1_bim_1_sem_alter, subject_grade_2_bim_1_sem_alter, subject_grade_1_bim_2_sem_alter, subject_grade_2_bim_2_sem_alter):

        alter = session.query(Grade).filter(Grade(id) == grade_id).all()

        alter[0].student_id = student_id_alter
        alter[0].subject_grade_1_bim_1_sem = subject_grade_1_bim_1_sem_alter
        alter[0].subject_grade_2_bim_1_sem = subject_grade_2_bim_1_sem_alter
        alter[0].subject_grade_1_bim_2_sem = subject_grade_1_bim_2_sem_alter        
        alter[0].subject_grade_2_bim_2_sem = subject_grade_2_bim_2_sem_alter

    def calculateAverage(grade_id_avg):

        # Reescrever

        grade_avg = session.query(Grade).filter(Grade(id) == grade_id_avg).all()

        avg_1_sem = (grade_avg[0].subject_grade_1_bim_1_sem + grade_avg[0].subject_grade_2_bim_1_sem ) / 2
        avg_2_sem = (grade_avg[0].subject_grade_1_bim_2_sem + grade_avg[0].subject_grade_2_bim_2_sem ) / 2

        return avg_1_sem, avg_2_sem
    
class ControllerSchoolCard:

    def listAll():
        pass
