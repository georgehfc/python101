# coding: utf-8
# 5. Faça um programa que peça cinco números e mostre qual o maior e qual o menor
numbers = []
for number in range(5):
    add = int(input("Digite o número {}: ".format(number + 1)))
    numbers.append(add)
print("O maior número é {} e o menor número é {}".format(max(numbers), min(numbers)))
