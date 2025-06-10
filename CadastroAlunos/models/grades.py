class Grades:
    def __init__(self,grades_id: int):
        self.grades_id = grades_id

    def __str__(self):
        return f"Grades ID: {self.grades_id}"