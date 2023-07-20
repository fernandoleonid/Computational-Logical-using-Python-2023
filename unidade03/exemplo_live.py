lista_clientes = []

resposta = 's'

while resposta == 's':
    nome_digitado = input("Digite seu nome: ")
    estado_digitado = input("Digite seu estado: ")

    cliente = {
        "nome": nome_digitado,
        "estado": estado_digitado
    }
    
    lista_clientes.append (cliente)

    resposta = input ("Deseja continuar [s/n]: ")

print (lista_clientes)