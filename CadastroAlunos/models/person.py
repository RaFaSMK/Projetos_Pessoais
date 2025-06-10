class Person:
    def __init__(self, name: str, cpf: int, adress: str, phone_number: int):
        self.name = name
        self.cpf = cpf
        self.adress = adress
        self.phone_number = phone_number

    def __str__(self):
        return f"{self.name} ({self.cpf}) - {self.adress}, {self.phone_number}"