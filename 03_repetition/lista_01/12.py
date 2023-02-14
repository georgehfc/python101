# coding: utf-8
# 12. Faça um programa que peça o nome de um aluno, depois cada uma das quatro
# disciplinas (Matemática, Português, Ciências e Comunicação) e depois as 4 notas
# da prova daquela disciplina. Mostre depois a média de cada disciplina.
# Se as quatro médias forem acima de 6, mostre a frase "aprovado". Caso uma das
# médias for abaixo de 6, mostrar a frase "reprovado na matéria (nome da matéria)",
# para cada uma das matérias com média abaixo do esperado

nome = input("Qual o seu nome? ")

# notas["Matemática"]
notas = {}
# medias["Matemática"]
medias = {}

for i in range(4):
    disc = input(f"Nome da Disciplina {i + 1}: ")
    notas[disc] = []
    media = 0

    for j in range(4):
        nota = input(f"Nota {j + 1}: ")
        notas[disc].append(float(nota))
        media = media + float(nota)

    media = media / 4
    medias[disc] = float(media)
    if media < 6:
        print(f"### Reprovado em {disc} com {media}")

print(f"Médias de {nome}:")
for disc, media in medias.items():
    print(f"{disc}: {media}")
