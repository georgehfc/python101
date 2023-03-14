from Funcoes import *

usuarios = {}
opcao = perguntar()

while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L":
    if opcao=="I":
        inserir(usuarios)
    elif opcao=="P":
        pesquisar(usuarios, input("Buscar por: "))
    elif opcao=="E":
        excluir(usuarios, input("Excluir: "))
    elif opcao=="L":
        listar(usuarios, input("Listar: "))

    opcao = perguntar()
