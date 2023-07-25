import os
from colorama import init, Fore
from cidades import *

init(autoreset=True)

def limpar_tela():
    os.system('cls' if os.name == "nt" else 'clear')

def pausar():
    input(f"{Fore.BLUE}Digite ENTER para continuar...")

def exibir_menu():
    print(f"{Fore.GREEN}===== MENU =====")
    print(f"{Fore.GREEN}1. Listar cidades")
    print(f"{Fore.GREEN}2. Adicionar cidade")
    print(f"{Fore.GREEN}3. Buscar cidade")
    print(f"{Fore.GREEN}4. Atualizar cidade")
    print(f"{Fore.GREEN}5. Excluir cidade")
    print(f"{Fore.GREEN}0. Sair")    

def processar_opcao(opcao):
    if opcao == "1":
        cidades = ler_cidades()
        for cidade in cidades:
            print(f"-> {Fore.GREEN}{cidade}")

    elif opcao == "2":
        nome_cidade = input("Digite o nome da cidade para cadastrar: ")
        adicionar_cidade(nome_cidade)
        print("Cidade cadastrada com sucesso!")

    elif opcao == "3":
        nome_cidade = input("Digite o nome da cidade a ser buscada: ")
        cidades_encontradas = buscar_cidade(nome_cidade)
        print("Cidades encontradas:")
        for cidade in cidades_encontradas:
            print(cidade)

    elif opcao == "4":
        nome_antigo = input("Digite o nome da cidade a ser atualizada: ")
        nome_novo = input("Digite o novo nome da cidade: ")
        if atualizar_cidade(nome_antigo, nome_novo):
            print("Cidade atualizada com sucesso!")
        else:
            print("Cidade não encontrada.")

    elif opcao == "5":
        nome_cidade = input("Digite o nome da cidade a ser excluída: ")
        if excluir_cidade(nome_cidade):
            print("Cidade excluída com sucesso!")
        else:
            print("Cidade não encontrada.")          

    elif opcao == "0":
        print("Saindo do Sistema...")
        exit(0)

    else:
        print(f"{Fore.RED}Opção inválida. Tente novamente.")

def executar_sistema():
    exibir_menu()
    opcao = input("Digite a opção desejada: ")
    limpar_tela()
    processar_opcao(opcao)
    pausar()
    executar_sistema()


executar_sistema()