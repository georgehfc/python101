# coding: utf-8
# 13.  Faça um programa que recebe um número e mostra uma lista de todos os
# número pares até o número informado, CONSIDERANDO o número informado
num = int(input("Número: "))
for i in range(0, num + 1, 2):
    print(i)
