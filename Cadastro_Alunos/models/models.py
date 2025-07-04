from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

USUARIO = "postgres" #Constantes para a string de conexão
SENHA = "250406"
HOST = "localhost"
BANCO = "cadastro_alunos"
PORT = "5432"

CONN = f"postgresql+psycopg2://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}" #String de conexão utilizando o psycopg2 pois é o drive que conecta com o PostgreSQL
engine = create_engine(CONN, echo=False) # Criação da engine, interface entre o ORM e o BD

Base = declarative_base() # Declarative base é uma classe base que todas as classes (tabelas) vão herdar

class Student(Base): # Cada classe que herda de Base, é uma tabela no BD
        __tablename__ = "student"
        id = Column(Integer(),primary_key=True)
        name = Column(String(50))
        cpf = Column(String(),nullable=False)
        adress = Column(String(100))
        phone_number = Column(Integer(),nullable=False)

class Teacher(Base):
        __tablename__ = "teacher"
        id = Column(Integer(),primary_key=True)
        name = Column(String(50))
        cpf = Column(String(),nullable=False)
        adress = Column(String(100))
        phone_number = Column(Integer(),nullable=False)
        
class Subject(Base):
    __tablename__ = "subject"
    id = Column(Integer(),primary_key=True)
    name = Column(String(50))
    teacher_id = Column(Integer(),ForeignKey("teacher.id"))
    student_id = Column(Integer(),ForeignKey("student.id"))

class Grade(Base):
      __tablename__ = "grade"
      id = Column(Integer(),primary_key=True)
      student_id = Column(Integer(),ForeignKey("student.id"))
      subject_id = Column(Integer,ForeignKey("subject.id"))
      subject_grade_1_bim_1_sem = Column(Float(2,1))
      subject_grade_2_bim_1_sem = Column(Float(2,1))
      subject_grade_1_bim_2_sem = Column(Float(2,1))
      subject_grade_2_bim_2_sem = Column(Float(2,1))

Base.metadata.create_all(engine)