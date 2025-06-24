from models.grade import Grade

class GradeDAO:
    @classmethod
    def save(cls, grade: Grade):
        with open("data/grades.txt","a") as arq:
            arq.write(f"{grade.student}|{grade.grade_id}")
    
    @classmethod
    def read(cls):
        try:
            with open("data/grades.txt","r") as arq:
                lines = arq.readlines()
        except FileNotFoundError:
            return "FileNotFound"
        
        grades_list = []

        for line in lines:
            parts = line.strip().split("|")
            grades_list.append(line[0],line[1])
        
        return grades_list