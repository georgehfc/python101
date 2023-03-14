# SIMULAR SORTEIO DE SELEÇÕES DA COPA DO MUNDO ⚽️
# A CADA LOOP PERGUNTAR PAÍS E GRUPO
# SE GRUPO JÁ TIVER CHEIO (4 PAÍSES) NÃO PERMITA ADICIONAR
# AO FINAL DAS 32 SELEÇÕES EXIBA OS 8 GRUPOS
from collections import Counter
from faker import Faker
import random

print("### 🎉🏆 TÁAAA NA TELA 🏆🎉 ###")
print("É O SORTEIO DA COPA DO MUNDO DE FUTEBOL! ⚽️")

groups = {}

# # DRAW SEQUENCE OF POSITIONS
# order = list(range(1,33))
# random.shuffle(order)

for i in range(32):
    # country = input(f"País #{i+1}: ")
    fake = Faker()
    country = fake.country()
    print(f"Adicionando {country}...")
    while country in groups:
        # country = input(f"País já sorteado. Tente outra seleção: ")
        country = fake.country()
        print(f"País já sorteado. Novo sorteio... {country}!")
    # group = int(input("Insira um grupo: "))
    group = random.randint(1,8)
    print(f"Grupo sortado: {group}!")

    while group>8 or group<1:
        group = int(input("Grupo inválido. Tente outro grupo: "))

    count = Counter(groups.values())
    while count[group]>3:
        # group = int(input("Grupo cheio. Tente outro grupo: "))
        group = random.randint(1,8)
        print(f"Grupo cheio. Novo sorteio... Grupo: {group}!")
    groups[country] = group

print("#"*10 + "\nOs 8 grupos foram fechados! 🏟\n" + "#"*10)
# print(groups)

# https://stackoverflow.com/questions/54249400/python-how-to-group-keys-that-have-the-same-values-in-a-dictionary
countries = set(groups.values())
world_cup = {}
for i in countries:
    world_cup[f"Grupo {i}"] = [k for k in groups.keys() if groups[k] == i]

print(world_cup)
