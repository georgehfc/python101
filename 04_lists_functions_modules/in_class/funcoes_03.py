def ficha_cadastro(nome, sobrenome, cep, data_nascimento):
    return {
        "nome": nome,
        "sobrenome": sobrenome,
        "cep": cep,
        "data_nascimento": data_nascimento
    }


nome_pessoa = input("Entre com seu nome: ")
sobrenome_pessoa = input("Entre com seu sobrenome: ")
cep_residencia = input("Entre com seu CEP: ")
nascimento = input("Entre com seu nascimento: ")

# parametros nomeados
ficha_preenchida = ficha_cadastro(
    data_nascimento=nascimento,
    nome=nome_pessoa,
    cep=cep_residencia,
    sobrenome=sobrenome_pessoa,
)
print(ficha_preenchida)
