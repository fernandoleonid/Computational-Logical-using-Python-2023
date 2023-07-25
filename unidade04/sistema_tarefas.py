import os
from manipulador_arquivo import *
from colorama import init, Fore

init(autoreset=True)

def pausar ():
    input("Digite ENTER para continuar...")

def processar_menu(opcao):
    if opcao == "1":
        tarefa = input ("Digite uma tarefa: ")
        escrever_arquivo("tarefas.txt", tarefa)
    elif opcao == "2":
        limpar_tela()
        print (f"{Fore.GREEN}#### TAREFAS ####")
        ler_arquivo("tarefas.txt")
        pausar()
    elif opcao == "0":
        print ("Saindo do sistema...")
        exit(0)
    else:
        print (f"{Fore.RED}Opção inválida. Tente novamente!")
        pausar()
    

def limpar_tela():
    os.system('cls' if os.name == "nt" else 'clear')

def exibir_menu():
    print (f"#### MENU ####")
    print (f"1 - Adicionar tarefa")
    print (f"2 - Ler tarefas")
    print (f"0 - Sair")

def executar_sistema():
    limpar_tela()
    exibir_menu()
    opcao = input("Digite uma opção: ")
    processar_menu(opcao)
    executar_sistema()


executar_sistema()