estoque = list()

produto = dict()

dados = dict()

clientes = list()

vendas = list()

qtd_estoque = list()

while True:

    print("-" * 15)

    print("Menu do Sistema: ")

    print("-" * 15)

    print("Digite [1] para cadastrar um produto.")

    print("Digite [2] para atualizar um produto.")

    print("Digite [3] para vender um produto.")

    print("Digite [4] para cadastrar um cliente.")

    print("Digite [5] para consultar um cliente.")

    print("Digite [6] para exibir todos os clientes cadastrados.")

    print("Digite [7] para consultar o estoque.")

    print("Digite [8] para consultar a venda total dos produtos.")

    print("Digite [0] para sair do sistema.")

    print("    -     ")

    opcao = (input("Digite uma opção: "))

    print("-" *15)

    if opcao == "1":

        nome = str(input("Informe o nome do produto: ")).strip().lower()


        if nome not in produto.values():

            produto['nome'] = nome

            print(" ")

            produto['preco'] = float(input("Informe o preço do produto: R$"))

            print(" ")

            produto['quantidade'] = int(input("Informe a quantidade em estoque: "))

            estoque.append(produto.copy())

            print("-" * 15)

            print("Produto adicionado com sucesso.")

            print("-" * 15)

        else:

            print("Produto já cadastrado.")

    elif opcao == "2":

        nome_produto = str(input("Informe o nome do produto: ")).strip().lower()

        print(" ")

        for produto in estoque:

            if produto['nome'] == nome_produto:

                preco = float(input("Informe o novo preço do produto: R$"))

                print(" ")

                quantidade = int(input("Informe a nova quantidade em estoque: "))

                print("-" * 15)

                produto['preco'] = preco

                produto['quantidade'] = quantidade

                print("Produto atualizado com sucesso.")

                print("-" * 15)

        if produto['nome'] != nome_produto:

            print("Produto não encontrado.")

    elif opcao == "3":

        nome = str(input("Informe o nome do produto: ")).strip().lower()

        if nome in produto.values():

            vendas.append(produto['preco'])

            qtd_estoque.append(produto['quantidade'])

            print("Produto vendido com sucesso.")

        else:

            print("Prduto não cadastrado.")

    elif opcao == "4":

        cliente = str(input("Digite o nome do cliente: ")).strip().lower()

        if cliente not in dados.values():

            dados['nome'] = cliente

            dados['idade'] = int(input("Digite a idade do cliente: "))

            dados['bairro'] = str(input("Digite o bairro do cliente: "))

            dados['endereço'] = str(input("Digite o endereço do cliente: "))

            dados['telefone'] = int(input("Digite o telefone do cliente: "))

            clientes.append(dados.copy())

            print("Cliente cadastrado com sucesso.")

            print("-" * 15)

        else:

            print("Cliente já cadastrado.")

    elif opcao == "5":

        cliente = str(input("Digite o nome do cliente: ")).strip().lower()

        if cliente in dados.values():

            print(dados['nome'])

        else:

            print("Cliente não cadastrado.")

    elif opcao == "6":

        for k, v in enumerate(clientes):

            print(f" {k:>5}")

            for valor in v.values():

                print(f' {str(valor):<14}')

            print()

    elif opcao == "7":

        print("------ ESTOQUE ------ ")

        print("   COD PRODUTO       PREÇO        QUANTIDADE")

        q_estoque = produto['quantidade']

        soma = q_estoque - 1

        valor = soma

        for k, v in enumerate(estoque):

            #print("   COD PRODUTO       PREÇO        QUANTIDADE")

            print(f" {k:>5}", end = ' ')

            for valor in v.values():

                print(f"{str(valor):<14}", end = ' ')

            print()

    elif opcao == "8":

        def somaL(vendas):

            soma = 0

            for i in vendas :

                soma = soma + i

            return soma

        soma = somaL(vendas)

        print(f"A soma total dos produtos vendidos é de R${soma:.2f}.")

    elif opcao == "0":

        print("Você saiu do sistema.")

        break

    else:

        print("Digite uma das quatro opções acima: ")

    resp = " "

    while resp not in 'SN':

        resp = input("Deseja continuar no sistema?[s/n]: ") .strip().upper()[0]

    if resp == 'N':

        break