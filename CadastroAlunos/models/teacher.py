from models.person import Person

class Teacher(Person):
    def __init__(self, name: str, cpf: int, adress: str, phone_number: int, teacher_id: int):
        super().__init__(name, cpf, adress, phone_number)
        self.teacher_id = teacher_id