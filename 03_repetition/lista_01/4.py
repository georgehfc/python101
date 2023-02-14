# coding: utf-8
# 4. Faça um programa que peça uma frase para a pessoa e mostre a quantidade de
# letras que tem na frase
phrase = input("Digite uma frase e contaremos a quantidade de letras: ")
counter = 0
for letter in phrase:
    if(letter != ' '):
        counter = counter + 1
print("{} letras foram encontradas.".format(counter))
