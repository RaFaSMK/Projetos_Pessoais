from person import Person

class Student(Person):
    def __init__(self, name: str, cpf: int, adress: str, phone_number: int,student_id: int):
        super().__init__(name,cpf,adress,phone_number)
        self.student_id = student_id

    def __str__(self):
        return f"Student ID: {self.student_id} - {super().__str__()}"