from models.teacher import Teacher

class Subject:
    def __init__(self, teacher: Teacher, subject_id: int, name: str):
        self.teacher = teacher
        self.subject_id = subject_id
        self.name = name