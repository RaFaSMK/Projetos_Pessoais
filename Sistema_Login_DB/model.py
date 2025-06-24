from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

USUARIO = "root"
SENHA = ""
HOST = "localhost"
BANCO = "login"
PORT = "3306"

CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"
engine = create_engine(CONN, echo=True)

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "Usuario"
    id = Column(Integer, primary_key=True)
    nome = Column(String(50),nullable=False)
    email = Column(String(50),nullable=False,unique=True)
    senha = Column(String(100),nullable=False)

Base.metadata.create_all(engine)