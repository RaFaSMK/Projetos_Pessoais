from models.subject import Subject

class Subject_DAO:
    @classmethod
    def save(cls, subject: Subject):
        with open("data/subjects.txt","a") as arq:
            arq.write(f"{subject.subject_id}|{subject.name}|{subject.teacher}")
        
    @classmethod
    def read(cls):
        try:
            with open("data/subjects.txt","r") as arq:
                lines = arq.readlines()
        except FileNotFoundError:
            return "FileNotFound"
        
        subjects_list = []

        for line in lines:
            parts = line.strip().split("|")
            subjects_list.append(line[0],line[1],line[2])
        
        return subjects_list