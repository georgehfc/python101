# coding: utf-8
# 6. Faça um programa que peça o nome da pessoa e a idade e diga se a pessoa já
# pode votar, se a pessoa já pode obter a carta de motorista
name = input("Digite o nome da pessoa: ")
age = int(input("Digite a idade da pessoa: "))
if age < 16:
    print("{} ainda n˜åo pode votar e nem obter a carta de motorista". format(name))
else:
    print("{} já pode votar e obter a carta de motorista". format(name))
