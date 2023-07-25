def ler_cidades():
    cidades = []
    for linha in open("cidades.txt", "r"):
        cidades.append(linha.strip().lower())
    return cidades

def adicionar_cidade(nome_cidade):
    arquivo = open("cidades.txt", "a")
    arquivo.write(nome_cidade + "\n")
    arquivo.close()

def buscar_cidade(nome_cidade):
    cidades = ler_cidades()
    cidades_encontradas = []
    for cidade in cidades:
        if nome_cidade.lower() == cidade:
            cidades_encontradas.append(cidade)
    return cidades_encontradas    

def adicionar_lista_cidades(cidades):
    arquivo = open("cidades.txt", "w")
    for cidade in cidades:
        arquivo.write(cidade + "\n")
    arquivo.close()


def atualizar_cidade(nome_antigo, nome_novo):
    cidades = ler_cidades()
    if cidades.count(nome_antigo) > 0:
        indice = cidades.index(nome_antigo)
        cidades[indice] = nome_novo
        adicionar_lista_cidades(cidades)
        return True
    else:
        return False
    
def excluir_cidade(nome_cidade):
    nome_cidade = nome_cidade.lower()
    cidades = ler_cidades()
    if cidades.count(nome_cidade) > 0:
        cidades.remove(nome_cidade)
        adicionar_lista_cidades(cidades)
        return True
    else:
        return False