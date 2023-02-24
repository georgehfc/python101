# Criação de uma lista com os nomes dos Jedi
jedi = ["Yoda", "Luke", "Obi-Wan", "Anakin"]

# Exibindo um valor específico da lista
print(jedi[2])

# Incluindo um valor no final da lista
jedi.append("Mace Windu")

# Incluindo um valor digitado no final da lista
jedi.append(input("Digite o nome de um Jedi: "))

# Incluindo um valor em uma posição específica da lista
jedi.insert(2, "Luminara")

# Incluindo um valor pelo usuário em uma posição específica da lista
jedi.insert(2, input("Digite o nome de um Jedi: "))

print("# Todos os jedis encontrados:")
# A variável assumirá cada um dos valores da lista
for nome in jedi:
    print(nome) # Para cada volta do loop, exibir o valor assumido

# Removendo o último valor inserido na lista
jedi.pop()
print(jedi)

# Removendo um valor em uma posição específica
jedi.pop(2)
print(jedi)

# Removendo um valor específico da lista
jedi.remove(input("Digite o nome de um Jedi: "))
print(jedi)
