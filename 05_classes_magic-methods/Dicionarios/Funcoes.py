def perguntar():
    return input("O que deseja realizar?\n" +
            "<I> - Para inserir um usuário\n" +
            "<P> - Para pesquisar um usuário\n" +
            "<E> - Para excluir um usuário\n" +
            "<L> - Para listar um usuário: ").upper()

def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()]=[input("Digite o nome: ").upper(), input("Digite a última data de acesso: "), input("Digite a última estação acessada: ").upper()]

def pesquisar(dicionario, busca):
    if busca.upper() in dicionario:
        print(f"{busca} existe!")
        return True
    else:
        print(f"{busca} não existe...")
        return False

def excluir(dicionario, retirar):
    if pesquisar(dicionario, retirar):
        dicionario.pop(retirar.upper())
        print(f"... mas usuário {retirar} foi removido.")
    else:
        return None

def listar(dicionario, listar):
    if pesquisar(dicionario, listar):
        print(dicionario.get(listar.upper()))
    else:
        return None
