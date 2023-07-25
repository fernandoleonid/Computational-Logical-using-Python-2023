lista = [
    {
        "nome": "pedro",
        "estado": "sp"  
    },
    {
        "nome": "hugo",
        "estado": "sp"  
    }
]

nome = input("Digite um nome: ")

for cliente in lista:
    if nome in cliente.values(): 
        print ("Exite o nome")
    else:
        print ("Não existe!")