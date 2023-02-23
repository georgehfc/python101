# 01 - Criar uma funcao que recebe um nome e
# devolve a frase "Boa noite, {nome}". E depois
# usar essa função e imprimir na tela.

def saudacao(nome):
    frase = "Boa noite, " + nome
    # frase = f"Boa noite, {nome}"
    return frase


nome_pessoa = input("Qual sua graça? ")
print(saudacao(nome_pessoa))
