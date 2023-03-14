# Criando as duas listas
personagens=[]
categorias=[]

# Executando um loop 10 vezes
for x in range(10):
    # Pedindo que o usuário informe um nome e colocando na lista de personagens
    personagens.append(input("Informe o nome do personagem: "))
    # Pedindo que o usuário informe a categoria e colocando na lista de categorias
    categorias.append(input("Informe a categoria do personagem: "))

# Executando um loop 10 vezes
for indice in range(10):
    # Exibindo a cada volta o que está contido em um índice de personagens e categorias
    print("O personagem {} é um(a) {}".format(personagens[indice], categorias[indice]))

#######

# Criando um dicionario vazio
dicionario = {}
# Exibindo o tipo do dicionário
print("O objeto dicionario é do tipo {}".format(type(dicionario)))
# Criando um dicionario com dados
dicionario = {"Yoda":"Mestre Jedi", "Mace Windu": "Mestre Jedi", "Anakin Skywalker":"Cavaleiro Jedi", "R2-D2":"Dróide", "Dex":"Balconista"}

# Exibindo todos os valores em um dicionario
for valor in dicionario.values():
    print(valor)

# Exibindo todas as chaves em um dicionario
for chave in dicionario.keys():
    print(chave)

# Exibindo o dicionário completo
for chave, valor in dicionario.items():
    print("O personagem {} é da categoria {}".format(chave, valor))

#######

# Zerando dicionário
dicionario = {}
# Incluindo dados no dicionario
dicionario["André David"] = "Professor"
# Pedindo para o usuário incluir dados no dicionário
nova_chave = input("Informe o nome do colaborador da FIAP: ")
novo_valor = input("Informe a função do colaborador da FIAP: ")
# dicionario[input("Informe o nome do colaborador da FIAP: ")] = input("Informe a função do colaborador da FIAP: ")
dicionario[nova_chave] = novo_valor
# Exibindo o dicionário completo
for chave, valor in dicionario.items():
    print("O colaborador {} desempenha a função de {}".format(chave, valor))

#######

# Criando um dicionario com dados
dicionario = {"Yoda":"Mestre Jedi", "Mace Windu": "Mestre Jedi", "Anakin Skywalker":"Cavaleiro Jedi", "R2-D2":"Dróide", "Dex":"Balconista"}
# Exibindo o dicionário completo
for chave, valor in dicionario.items():
    print("O personagem {} é da categoria {}".format(chave, valor))
# Removendo o item cuja chave é R2-D2
dicionario.pop("R2-D2")
# Removendo o último item
dicionario.popitem()
# Exibindo o dicionário completo após a remoção
for chave, valor in dicionario.items():
    print("O personagem {} é da categoria {}".format(chave, valor))
# Removendo todos os itens do dicionário
dicionario.clear()

#######

# Criando o dicionário dos contatos
contatos = {
    "Clark Kent":
        {"Celular":"123456",
         "Email":"super@krypton.com"},
    "Bruce Wayne":
        {"Celular":"654321",
         "Email":"bat@caverna.com.br"}
}
# Esse for passará por todos os items do dicionário contatos, com a variável "contato" contendo as chaves desses items e o objeto formas contendo os valores, que são os dicionários de formas de contatos
for contato, formas in contatos.items():
    # Para cada item encontrado no dicionário anterior, que estão contidos no dicionário "formas", vamos recuperar as chaves "celular" e "email" e seus valores
    for celular, email in formas.items():
        # Exibimos aqui o nome do contato e as suas formas de contato
        print("O contato {} pode ser encontrado no celular {} e no email {}".format(contato, celular, email))
