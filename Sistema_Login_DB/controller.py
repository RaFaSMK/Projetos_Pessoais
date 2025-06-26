from sqlalchemy.orm import sessionmaker
from model import Usuario, engine
import bcrypt

Session = sessionmaker(bind=engine)
session = Session()

class ControllerCadastro:
    def verificarSenha(self,senha):
        if len(senha) < 8 or not any(char in senha for char in "@#$%"):
            return "A senha deve conter no mínimo 8 caractéres e um símbolo (@,#,$,%)!"
        return senha

    def criptografarSenha(self, senha):
        senha_valida = self.verificarSenha(senha)
        if senha_valida != senha:
            return senha_valida  # retorna mensagem de erro
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(senha.encode('utf-8'), salt).decode('utf-8')
    
    @staticmethod
    def verificar_senha(senha, hash_senha):
        return bcrypt.checkpw(senha.encode('utf-8'), hash_senha.encode('utf-8'))

    def cadastrarUsuario(self,nomeCadastrar,emailCadastrar,senhaCadastrar):
        
        emailCadastrar = emailCadastrar.strip().lower()
        senhaCriptoGrafada = self.criptografarSenha(senhaCadastrar)

        if senhaCriptoGrafada.startswith("A senha"):
            return senhaCriptoGrafada

        x = Usuario(nome = nomeCadastrar,
                    email = emailCadastrar,
                    senha = senhaCriptoGrafada)

        session.add(x)
        session.commit()

class ControllerLogin(ControllerCadastro):
    def verificarLogin(self,emailLogin,senhaLogin):
        user = session.query(Usuario).filter(Usuario.email == emailLogin).first()

        if user and self.verificar_senha(senhaLogin,user.senha):
            return "Login efetuado com sucesso!"
        else:
            return "E-mail não cadastrado"