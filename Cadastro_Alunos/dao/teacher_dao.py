from models.teacher import Teacher

class TeacherDAO:
    @classmethod
    def save(cls, teacher: Teacher):
        with open("data/teachers.txt", "a") as arq:
            arq.write(f"{teacher.name}|{teacher.cpf}|{teacher.adress}|{teacher.phone_number}|{teacher.teacher_id}")
    
    @classmethod
    def read(cls):
        try:
            with open("data/teachers.txt","r") as arq:
                lines = arq.readlines()
        except FileNotFoundError:
            return "FileNotFound"
        
        teacher_list = []

        for line in lines:
            parts = line.strip().split("|")
            teacher_list.append(Teacher(line[0],line[1],line[2],line[3],line[4]))

        return teacher_list