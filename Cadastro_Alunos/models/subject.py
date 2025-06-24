from models.teacher import Teacher

class Subject:
    def __init__(self, subject_id: int, name: str, teacher: Teacher):
        self.subject_id = subject_id
        self.name = name
        self.teacher = teacher