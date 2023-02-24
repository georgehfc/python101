# FEITO PELO PROFESSOR
# data_nascimento é opcional
def ficha_cadastro(nome, sobrenome, cep, data_nascimento = None):
    return {
        "nome": nome,
        "sobrenome": sobrenome,
        "cep": cep,
        "data_nascimento": data_nascimento
    }


def obter_valor(nome_campo):
    valor_campo = input(f"Entre com seu {nome_campo}: ")
    while valor_campo == "":
        print(f"{nome_campo} Invalido! ")
        valor_campo = input(f"Entre com seu {nome_campo}: ")
    return valor_campo

# PARÊNTESIS NÃO OBRIGATÓRIO
def mostrar_menu():
    texto_menu = "Digite S para SAIR, \nP para mostrar todos os cadastros\nou qualquer outra tecla para cadastrar uma nova gente: "
    return texto_menu


def obter_escolha():
    escolha = input(mostrar_menu())
    return escolha

lista_gentes = []

print("## Cadastro de gentes ##")
continuar = obter_escolha()

while continuar != "S" and continuar != 's':
    if continuar == "p" or continuar == "P":
        for gente in lista_gentes:
            print(gente)
    else:
        nome_pessoa = obter_valor("Nome")
        sobrenome_pessoa = obter_valor("Sobrenome")
        cep_residencia = obter_valor("Cep")

        data_nascimento = input("Entre com sua Data de Nascimento: ")
        if data_nascimento == "":
            data_nascimento = None

        ficha_preenchida = ficha_cadastro(
            nome=nome_pessoa,
            cep=cep_residencia,
            sobrenome=sobrenome_pessoa,
            data_nascimento=data_nascimento
        )
        lista_gentes.append(ficha_preenchida)

        print('!!! PESSOA CADASTRADA COM SUCESSO !!!')

    continuar = obter_escolha()

print("Pessoas cadastradas: ")

for gente in lista_gentes:
    print(gente)

print("Final do programa.")
