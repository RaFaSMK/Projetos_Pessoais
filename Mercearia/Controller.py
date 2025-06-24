from Models import Categoria,Estoque,Produtos,Fornecedor,Pessoa,Funcionario,Venda
from DAO import DaoCategoria,DaoVenda,DaoEstoque,DaoPessoa,DaoFornecedor,DaoFuncionario
from datetime import datetime


'''
return 1: produto não existe
return 2: quantidade vendida nao tem em estoque
return 3: venda efetuada com sucesso
'''

class ControllerCategoria:
    def cadastraCategoria(self, novaCategoria):
        existe = False
        x = DaoCategoria.ler()
        for i in x:
            if i.categoria == novaCategoria:
                existe = True
        
        if not existe:
            DaoCategoria.salvar(novaCategoria)
            print("\nCategoria cadastrada com sucesso!")
        else:
            print("\nA categoria que deseja cadastrar ja existe!")

    def removerCategoria(self, categoriaRemover):
        x = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == categoriaRemover, x))
        
        if len(cat) <= 0:
            print("\nA categoria que deseja remover não existe!")

        else:
            for i in range(len(x)):
                if x[i].categoria == categoriaRemover:
                    del x[i]
                    break
            print("\nCategoria removida com sucesso!")
        
        with open("categoria.txt","w") as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines("\n")
            
        estoque = DaoEstoque.ler()
        
        estoque = list(map(lambda x: Estoque(Produtos(x.produto.nome, x.produto.preco, "Sem categoria"), x.quantidade) if(x.produto.categoria == categoriaRemover) else(x), estoque))

        with open("estoque.txt","w") as arq:
            for i in estoque:
                arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" + i.produto.categoria + "|" + str(i.quantidade))
                arq.writelines("\n")
                
    def alterarCategoria(self, categoriaAlterar, categoriaAlterada):
        x = DaoCategoria.ler()

        cat = list(filter(lambda x: x.categoria == categoriaAlterar, x))

        if len(cat) > 0:
            cat1 = list(filter(lambda x: x.categoria == categoriaAlterada, x))
            if len(cat1) == 0:
                x = list(map(lambda x: Categoria(categoriaAlterada) if(x.categoria == categoriaAlterar) else(x),x))
                print("\nA alteração foi efetuada com sucesso")
            
                estoque = DaoEstoque.ler()
                        
                estoque = list(map(lambda x: Estoque(Produtos(x.produto.nome, x.produto.preco, "Categoria alterada"), x.quantidade) if(x.produto.categoria == categoriaAlterar) else(x), estoque))
                with open("estoque.txt","w") as arq:
                    for i in estoque:
                        arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" + i.produto.categoria + "|" + str(i.quantidade))
                        arq.writelines("\n")

            else:
                print("\nA categoria para qual deseja alterar ja existe")
        else:
            print("\nA categoria que deseja alterar não existe")
        
        with open("categoria.txt","w") as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines("\n")
        
    def mostrarCategoria(self):
        categorias = DaoCategoria.ler()

        if len(categorias) == 0:
            print("Categoria vazia")
        else:
            for i in categorias:
                print(f"Categoria: {i.categoria}")

class ControllerEstoque:
    def cadastrarProduto(self, nome, preco, categoria, quantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        h = list(filter(lambda x: x.categoria == categoria, y))
        est = list(filter(lambda x: x.produto.nome == nome, x))

        if len(h) > 0:
            if len(est) == 0:
                produto = Produtos(nome,preco,categoria)
                DaoEstoque.salvar(produto, quantidade)
                print("\nProduto cadastrado com sucesso!")
            else:
                print("\nProduto ja existe em estoque!")
        else:
            print("\nCategoria inexistente!")

    def removerProduto(self,nome):
        x = DaoEstoque.ler()
        est = list(filter(lambda x: x.produto.nome == nome, x))

        if len(est) > 0:
            for i in range(len(x)):
                if x[i].produto.nome == nome:
                    del x[i]
                    break            

        else:
            print("\nO produto que deseja remover não existe!")

        with open("estoque.txt","w") as arq:
            for i in x:
                arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" +
                           i.produto.categoria + "|" + str(i.quantidade))
                arq.writelines("\n")
    
    def alterarProduto(self,nomeAlterar,novoNome,novoPreco,novaCategoria,novaQuantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        h = list(filter(lambda x: x.categoria == novaCategoria,y))
        
        if len(h) > 0:
            est = list(filter(lambda x: x.produto.nome == nomeAlterar,x))
            if len(est) > 0:
                est = list(filter(lambda x: x.produto.nome == novoNome,x))
                if len(est) == 0:
                    x = list(map(lambda x: Estoque(Produtos(novoNome,novoPreco,novaCategoria),novaQuantidade) if (x.produto.nome == nomeAlterar) else(x),x))
                    print("\nProduto alterado com sucesso!")
                else:
                    print("\nProduto ja cadastrado!")
            else:
                print("\nO produto que deseja alterar não existe!")

            with open("estoque.txt","w") as arq:
                for i in x:
                    arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" +
                           i.produto.categoria + "|" + str(i.quantidade))
                    arq.writelines("\n")
        else:
            print("\nA categoria informada não existe")
    
    def mostrarEstoque(self):
        estoque = DaoEstoque.ler()
        if len(estoque) == 0:
            print("\nEstoque vazio")
        else:
            print("\n==========Produto==========")
            for i in estoque:
                print(f"Nome: {i.produto.nome}\n"
                      f"Preco: {i.produto.preco}\n"
                      f"Categoria: {i.produto.categoria}\n"
                      f"Quantidade: {i.quantidade}\n")
            print("--------------------")
                
class ControllerVenda:
    def cadastrarVenda(self,nomeProduto, vendedor, comprador, quantidadeVendida):
        x = DaoEstoque.ler()
        temp = []
        existe = False
        quantidade = False
        
        for i in x:
            if existe == False:
                if i.produto.nome == nomeProduto:
                    existe = True
                    if i.quantidade >= quantidadeVendida:
                        quantidade = True
                        i.quantidade = int(i.quantidade) - int(quantidadeVendida)
                        vendido = Venda(Produtos(i.produto.nome,i.produto.preco,i.produto.categoria),vendedor, comprador, quantidadeVendida)
                        valorCompra = int(quantidadeVendida) * int(i.produto.preco)
                        DaoVenda.salvar(vendido)
                        print("\nVenda cadastrada com sucesso!")
            temp.append(Estoque(Produtos(i.produto.nome,i.produto.preco,i.produto.categoria),i.quantidade))
        
        with open ("estoque.txt","w") as arq:
            arq.write("")

        for i in temp:
            with open("estoque.txt","a") as arq:
                arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" + i.produto.categoria + "|" + str(i.quantidade))
                arq.writelines("\n")
        
        if existe == False:
            #print("O produto não existe")
            return 1
        elif not quantidade:
            #print("Há quantidade vendida não contem em estoque")
            return 2
        else:
            #print("Venda realizada com sucesso")
            return 3,valorCompra
            
    def relatorioProdutos(self):

        vendas = DaoVenda.ler()
        produtos = []
        a = 1

        for i in vendas:
            nome = i.itensVendidos.nome
            quantidade = i.quantidadeVendida
            tamanho = list(filter(lambda x: x["produto"] == nome, produtos))
            if len(tamanho) > 0:
                produtos = list(map(lambda x: {"produto": nome, "quantidade": int(x["quantidade"]) + int(quantidade)} if(x["produto"] == nome) else(x),produtos))
            else:
                produtos.append({"produto": nome, "quantidade": int(quantidade)})            
        ordenado = sorted(produtos, key=lambda k: k["quantidade"], reverse=True)

        print("\nEsses são os produtos mais vendidos: ")
        for i in ordenado:
            print(f"\n==========Produto [{a}]==========")
            print(f"Produto: {i['produto']}\n"
                    f"Quantidade: {i['quantidade']}\n")
            a += 1

    def mostrarVenda(sellf,dataInicio,dataTermino):
        vendas = DaoVenda.ler()
        dataInicio1 = datetime.strptime(dataInicio,'%d/%m/%Y')
        dataTermino1 = datetime.strptime(dataTermino,'%d/%m/%Y')

        vendasSelecionadas = list(filter(lambda x: datetime.strptime(x.data,'%d/%m/%Y') >= dataInicio1 
                                         and datetime.strptime(x.data,'%d/%m/%Y') <= dataTermino1, vendas))
        
        cont = 1
        total = 0

        for i in vendasSelecionadas:
            print(f"\n==========Venda [{cont}]==========")
            print(f"Nome: {i.itensVendidos.nome}\n"
                  f"Categoria: {i.itensVendidos.categoria}\n"
                  f"Data: {i.data}\n"
                  f"Quantidade: {i.quantidadeVendida}\n"
                  f"Cliente: {i.comprador}\n"
                  f"Vendedor: {i.vendedor}\n")
            total += int(i.itensVendidos.preco) * int(i.quantidadeVendida)
            cont += 1
        print(f"Total vendido: {total}") 
    
class ControllerFornecedor:
    def cadastrarFornecedor(self, nome, cnpj, telefone, categoria):
        
        lista_fornecedores = DaoFornecedor.ler()
        listaCnpj = list(filter(lambda x: x.cnpj == cnpj, lista_fornecedores))
        listaTelefone = list(filter(lambda x: x.telefone == telefone, lista_fornecedores))

        if len(listaCnpj) > 0:
            print("\nEste CNPJ ja existe!")
        elif len(listaTelefone) > 0:
            print("\nEste telefone ja existe")
        else:
            if len(cnpj) == 14 and len(telefone) <= 11 and len(telefone) >= 10:
                DaoFornecedor.salvar(Fornecedor(nome, cnpj, telefone, categoria))
                print("\nFornecedor cadastrado com sucesso")

            else:
                print("\nDigite um cpf ou telefone válido")
    
    def alterarFornecedor(self, nomeAlterar,novoNome,novoCnpj,novoTelefone,novaCategoria):
        x = DaoFornecedor.ler()

        est = list(filter(lambda x: x.nome == nomeAlterar, x))
        if len(est) > 0:
            est = list(filter(lambda x: x.cnpj == novoCnpj, x))
            if len(est) == 0:
                x = list(map(lambda x: Fornecedor(novoNome, novoCnpj, novoTelefone, novaCategoria) if(x.nome == nomeAlterar) else(x), x))
                print("\nFornecedor alterado com sucesso")
            else:
                print("\nEsse CNPJ já exste")
        else:
            print("\nO fornecedor que deseja alterar não existe")
        
        with open("fornecedores.txt","w") as arq:
            for i in x:
                arq.writelines(i.nome + "|" + i.cnpj + "|" + i.telefone + "|" + str(i.categoria))
                arq.writelines("\n")

    def removerFornecedor(self,nome):
        x = DaoFornecedor.ler()

        est = list(filter(lambda x: x.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del x[i]
                    break
        else:
            print("\nEsse fornecedor que esta tentando remover não existe")
            return None

        with open("fornecedores.txt","w") as arq:
            for i in x:
                arq.writelines(i.nome + "|" + i.cnpj + "|" + i.telefone + "|" + str(i.categoria))
                arq.writelines("\n")
            print("\nFornecedor removido com sucesso")

    def mostrarFornecedor(self):
        fornecedores = DaoFornecedor.ler()
        if len(fornecedores) == 0:
            print("\nLista de fornecedores está vazia")
        else:
            print("\n==========Fornecedores==========")
            for i in fornecedores:
                print(f"Categoria fornecida: {i.categoria} \n"
                    f"Nome: {i.nome} \n"
                    f"Telefone: {i.telefone} \n"
                    f"Cnpj: {i.cnpj}\n")
            print("--------------------")

class ControllerCliente:
    def cadastrarCliente(self,nome,telefone,cpf,email,endereco):
        x = DaoPessoa.ler()

        listaCpf = list(filter(lambda x: x.cpf == cpf, x))
        listaTelefone = list(filter(lambda x: x.telefone == telefone, x))

        if len(listaCpf) > 0:
            print("\nEste CPF ja existe!")
        elif len(listaTelefone) > 0:
            print("\nEste telefone ja existe")
        else:
            if len(cpf) == 11 and len(telefone) <= 11 and len(telefone) >= 10:
                DaoPessoa.salvar(Pessoa(nome, telefone, cpf, email, endereco))
                print("\nCliente cadastrado com sucesso")
            else:
                print("\nDigite um cpf ou telefone válido")
        
    def alterarCliente(self, nomeAlterar, novoNome, novoTelefone,novoCpf , novoEmail, novoEndereco):
        x = DaoPessoa.ler()

        est = list(filter(lambda x: x.nome == nomeAlterar, x))
        if len(est) > 0:
            est = list(filter(lambda x: x.cpf == novoCpf, x))
            if len(est) == 0:
                x = list(map(lambda x: Pessoa(novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco) if(x.nome == nomeAlterar) else(x), x))
                print("\nCliente alterado com sucesso")
            else:
                print("\nEsse CPF já exste")
        else:
            print("\nO cliente que deseja alterar não existe")

        with open("clientes.txt","w") as arq:
            for i in x:
                arq.writelines(i.nome + "|" + i.telefone + "|" + i.cpf + "|" + i.email + "|" + i.endereco)
                arq.writelines("\n")
                    
    def removerCliente(self,nome):
        x = DaoPessoa.ler()
        est = list(filter(lambda x: x.nome == nome, x))

        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del x[i]
                    break
        else:
            print("\nO cliente que deseja remover não existe")
            return None
        
        with open("clientes.txt","w") as arq:
            for i in x:
                arq.writelines(i.nome + "|" + i.telefone + "|" + i.cpf + "|" + i.email + "|" + i.endereco)
                arq.writelines("\n")
            print("\nCliente removido com sucesso")

    def mostrarCliente(self):
        clientes = DaoPessoa.ler()
        if len(clientes) == 0:
            print("\nLista de clientes está vazia")
        else:
            print("\n==========Clientes==========")
            for i in clientes:
                print(f"Nome: {i.nome}\n"
                    f"Telefone: {i.telefone}\n"
                    f"Endereco: {i.endereco} \n"
                    f"Email: {i.email}\n"
                    f"CPF: {i.cpf}\n")
            print("--------------------")

class ControllerFuncionario:
    def cadastrarFuncionario(self,clt,nome,telefone,cpf,email,endereco):
        x = DaoFuncionario.ler()

        listaCpf = list(filter(lambda x: x.cpf == cpf, x))
        listaClt = list(filter(lambda x: x.clt == clt, x))

        if len(listaCpf) > 0:
            print("\nEste CPF ja existe!")
        elif len(listaClt) > 0:
            print("\nJa existe um funcionário com essa CLT")
        else:
            if len(cpf) == 11 and len(telefone) <= 11 and len(telefone) >= 10:
                DaoFuncionario.salvar(Funcionario(clt, nome, telefone, cpf, email, endereco))
                print("\nFuncionario alterado com sucesso")
            else:
                print("\nDigite um cpf ou telefone válido")
        
    def alterarFuncionario(self, nomeAlterar, novoClt, novoNome, novoTelefone,novoCpf , novoEmail, novoEndereco):
        x = DaoFuncionario.ler()

        est = list(filter(lambda x: x.nome == nomeAlterar, x))
        if len(est) > 0:
            x = list(map(lambda x: Funcionario(novoClt,novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco) if(x.nome == nomeAlterar) else(x), x))
            print("\nFuncionario alterado com sucesso")
        else:
            print("\nO funcionario que deseja alterar não existe")

        with open("funcionarios.txt","w") as arq:
            for i in x:
                arq.writelines(i.clt + "|" + i.nome + "|" + i.telefone + "|" + i.cpf + "|" + i.email + "|" + i.endereco)
                arq.writelines("\n")
    
    def removerFuncionario(self,nome):
        x = DaoFuncionario.ler()
        est = list(filter(lambda x: x.nome == nome, x))

        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del x[i]
                    break
        else:
            print("\nO funcionario que deseja remover não existe")
            return None
        
        with open("funcionarios.txt","w") as arq:
            for i in x:
                arq.writelines(i.clt + "|"+ i.nome + "|" + i.telefone + "|" + i.cpf + "|" + i.email + "|" + i.endereco)
                arq.writelines("\n")
            print("\nFuncionario removido com sucesso")

    def mostrarFuncionario(self):
        funcionarios = DaoFuncionario.ler()
        if len(funcionarios) == 0:
            print("\nLista de funcionarios está vazia")
        else:
            print("\n==========Funcionarios==========")
            for i in funcionarios:
                print(f"Nome: {i.nome}\n"
                    f"Telefone: {i.telefone}\n"
                    f"Endereco: {i.endereco} \n"
                    f"Email: {i.email}\n"
                    f"CPF: {i.cpf}\n"
                    f"CLT: {i.clt}\n")
            print("--------------------")