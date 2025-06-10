class Subject:
    def __init__(self,subject_id: int, name: str):
        self.subject_id = subject_id
        self.name = name
    
    def __str__(self):
        return f"Subject ID: {self.subject_id} - {self.name}"