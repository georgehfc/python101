# data_nascimento é opcional
def ficha_cadastro(nome, sobrenome, cep, data_nascimento=None):
    return {
        "nome": nome,
        "sobrenome": sobrenome,
        "cep": cep,
        "data_nascimento": data_nascimento
    }


nome_pessoa = input("Entre com seu nome: ")
sobrenome_pessoa = input("Entre com seu sobrenome: ")
cep_residencia = input("Entre com seu CEP: ")


# parametros nomeados
ficha_preenchida = ficha_cadastro(
    nome=nome_pessoa,
    cep=cep_residencia,
    sobrenome=sobrenome_pessoa,
)
print(ficha_preenchida)
