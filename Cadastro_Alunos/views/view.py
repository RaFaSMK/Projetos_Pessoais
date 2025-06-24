from controllers.student_controller import StudentController
import os.path

def createFiles(*args):
    for i in args:
        if not os.path.exists(i):
            with open(i,"w") as arq:
                arq.write("")

createFiles("data/grades.txt","data/students.txt","data/subjects.txt","data/teachers.txt")

if __name__ == "__main__":
    while True:
        name = input("name: ")
        cpf = input("cpf: ")
        adress = input("adress: ")
        phone_number = input("phone_number: ")
        student_id = input("student_id: ")
        subject = input("subject: ")
        StudentController.registerStudent(name, cpf, adress, phone_number, student_id, subject)
        break