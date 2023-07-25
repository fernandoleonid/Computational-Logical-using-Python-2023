def escrever_arquivo(nome_arquivo, conteudo):
    arquivo = open(nome_arquivo, "a")
    arquivo.write(conteudo + "\n")
    arquivo.close()


def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, "r")
    conteudo = arquivo.read()
    arquivo.close()
    print(f"{conteudo}")