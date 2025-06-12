from models.student import Student

class Student_DAO:
    @classmethod
    def save(cls, student: Student):
        with open("data/students.txt","a") as arq:
            arq.write(f"{student.name}|{student.cpf}|{student.adress}|{student.phone_number}|{student.student_id}\n")
    
    @classmethod
    def read(cls):
        try:
            with open("data/students.txt","r") as arq:
                lines = arq.readlines()

        except FileNotFoundError:
            return "FileNotFound"

        students_list = []
        
        for line in lines:
            parts = line.strip().split("|")
            students_list.append(Student(parts[0],parts[1],parts[2],parts[3],parts[4]))

        return students_list