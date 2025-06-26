from model import Usuario
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import bcrypt
import hashlib

def retorna_session():
    USUARIO = "root"
    SENHA = ""
    HOST = "localhost"
    BANCO = "login"
    PORT = "3306"

    CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"

    engine = create_engine(CONN, echo=True)
    
    Session = sessionmaker(bind=engine)
    return Session()

class ControllerCadastro:
    @classmethod
    def verifica_dados(cls, nome, email, senha):
        if len(nome) > 50 or len(nome) < 3:
            return 2
        if len(email) > 200:
            return 3
        if len(senha) > 100 or len(senha) < 8:
            return 4
    
        return 1
    
    @classmethod
    def cadastrarUsuario(cls,nome,email,senha):
        session = retorna_session()
        usuario = session.query(Usuario).filter(Usuario.email == email).all()

        if len(usuario) > 0:
            return 5

        dados_verificados = cls.verifica_dados(nome,email,senha)

        if dados_verificados != 1:
            return dados_verificados

        try:
            senha = hashlib.sha256(senha.encode()).hexdigest()
            x = Usuario(nome = nome,email = email,senha = senha)
            session.add(x)
            session.commit()
            return 1

        except:
            return 6
        
class ControllerLogin():
    @classmethod
    def login(cls,email,senha):
        session = retorna_session()
        senha = hashlib.sha256(senha.encode()).hexdigest()
        
        logado = session.query(Usuario).filter(Usuario.email == email).filter(Usuario.senha == senha).all()
        
        if len(logado) == 1:
            return {'logado' : True, 'id': logado[0].id}
        else:
            return False