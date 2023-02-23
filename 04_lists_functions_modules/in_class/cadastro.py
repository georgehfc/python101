def ficha_cadastro(nome, sobrenome, cep, nascimento=None):
    # RETORNAR DICT
    return {
        "nome": nome,
        "sobrenome": sobrenome,
        "cep": cep,
        "nascimento": nascimento
    }

user_nome = input("Entre com seu nome: ")
user_sobrenome = input("Entre com seu sobrenome: ")
user_cep = input("Entre com seu CEP: ")
user_nascimento = input("Entre com sua data de nascimento: ")

ficha = ficha_cadastro(
    nome = user_nome,
    sobrenome = user_sobrenome,
    cep = user_cep
    # nascimento = user_nascimento
)

# PARÂMETROS NOMEADOS
ficha = ficha_cadastro(
    # nome=nome
    )
print(ficha)
