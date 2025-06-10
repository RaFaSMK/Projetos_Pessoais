from person import Person

class Teacher(Person):
    def __init__(self, name: str, cpf: int, adress: str, phone_number: int, teacher_id: int):
        super().__init___(name,cpf,adress,phone_number)
        self.teacher_id = teacher_id
        
    def __str__(self):
        return f"Teacher ID: {self.teacher_id} - {super().__str__()}"