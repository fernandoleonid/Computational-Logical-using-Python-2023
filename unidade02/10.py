# 10. Crie um programa que exiba um menu 
# com 5 opções para o usuário. 
# A última opção deve ser "0" para sair 
# do programa. Cada opção do menu deve 
# exibir informações relevantes, sem 
# interação do usuário.

opcao = None

while opcao != 0:

    print ("Menu:")
    print ("1 - Opção 1")
    print ("2 - Opção 2")
    print ("3 - Opção 3")
    print ("4 - Opção 4")
    print ("5 - Opção 5")
    print ("0 - Sair")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        print ("Executando a opção 1...")
    elif opcao == 2:
        print ("Executando a opção 2...")
    elif opcao == 3:
        print ("Executando a opção 3...")
    elif opcao == 4:
        print ("Executando a opção 4...")
    elif opcao == 5:
        print ("Executando a opção 5...")
    elif opcao == 0:
        print ("Saindo do sistema...")
    else:
        print ("Opção inválida. Tente novamente!")
