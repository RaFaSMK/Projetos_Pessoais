from controller import ControllerCadastro,ControllerLogin

if __name__ == "__main__":
    while True:
        local = input("\nDigite 1 para realizar o seu cadastro\n"
                      "Digite 2 para realizar o seu login\n"
                      "Digite 3 para sair do programa\n\n")
        
        if local == "1":
            cadastro = ControllerCadastro()
            nomeCadastro = input("\nInforme seu nome para cadastro: \n")
            emailCadastro = input("Informe um e-mail válido para cadastro: \n")
            senhaCadastro = input("Informe a sua senha para cadastro: \n")
            print(cadastro.cadastrarUsuario(nomeCadastro,emailCadastro,senhaCadastro))

        elif local == "2":
            login = ControllerLogin()
            emailLogin = input("\nInforme um e-mail válido para login: \n")
            senhaLogin = input("Informe a sua senha para login: \n")
            emailLogin = emailLogin.strip().lower()
            print(login.verificarLogin(emailLogin,senhaLogin))

        elif local == "3":
            print("\nSaindo do programa")
            break

        else:
            print("\nDigite um número válido!")