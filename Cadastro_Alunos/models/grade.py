from models.student import Student

class Grade:
    def __init__(self, student: Student, grade_id: int):
        self.student = student
        self.grade_id = grade_id