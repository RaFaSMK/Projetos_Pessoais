from controller import ControllerCadastro, ControllerLogin

if __name__ == "__main__":
    while True:

        print("=========== [MENU] ===========")
        decidir = int(input("\nDigite 1 para realizar o seu cadastro\n"
                      "Digite 2 para realizar o seu login\n"
                      "Digite 3 para sair do programa\n\n"))
        
        if decidir == 1:
            nomeCadastro = input("\nInforme seu nome para cadastro: \n")
            emailCadastro = input("Informe um e-mail válido para cadastro: \n")
            senhaCadastro = input("Informe a sua senha para cadastro: \n")
            resultado = ControllerCadastro.cadastrarUsuario(nomeCadastro,emailCadastro,senhaCadastro)

            if resultado == 2:
                print("Tamanho do nome digitado inválido")
            elif resultado == 3:
                print("Email maior que 200 caracteres")
            elif resultado == 4:
                print("Tamanho da senha inválido")
            elif resultado == 5:
                print("Email ja cadastrado")
            elif resultado == 6:
                print("Erro interno do sistema")
            elif resultado == 1:
                print("Cadastro realizado com sucesso")

        elif decidir == 2:
            emailLogin = input("\nInforme um e-mail válido para login: \n")
            senhaLogin = input("Informe a sua senha para login: \n")
            resultado = ControllerLogin.login(emailLogin,senhaLogin)
            if not resultado:
                print("Email ou senha inválidos")
            else:
                print(resultado)

        elif decidir == 3:
            print("\nSaindo do programa") 
            break

        else:
            print("\nDigite um número válido!")