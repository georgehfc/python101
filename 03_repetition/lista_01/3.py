# coding: utf-8
# 3. Faça um programa que peça 2 números e mostre o resultado das 4 operacoes entre os dois
# números: soma, subtração, divisão e multiplicação
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
print("A soma é: {}".format(n1 + n2))
print("A subtração é: {}".format(abs(n1 - n2)))
print("A divisão é: {:.1f}".format(max(n1, n2) / min(n1, n2)))
print("A multiplicação é: {}".format(n1 * n2))
