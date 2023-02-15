# coding: utf-8
# 18. Crie um programa que pede números de 1 a 1000, e depois mostre quais são
# maiores que 500 e quais são menores. A quantidade de números informados tem
# que ser maior ou igual a 10, e menor e igual a 20
entradas = []

print("(Digite 0 para sair)")
num = int(input("Digite um número de 1 a 1000: "))
while num != 0:
    if num > 0 and num <= 1000:
        entradas.append(num)
    num = int(input("Digite um número de 1 a 1000: "))

if len(entradas) < 10 or len(entradas) > 20:
    print(f"Quantidade inválida de números fornecidos. ({len(entradas)})")
else:
    print('#' * 10)
    maiores = []
    print("Os números maiores que 500 são:")
    for i in entradas:
        if i > 500:
            maiores.append(i)
    print(maiores)

    menores = []
    print("Os números menores ou iguais a 500 são:")
    for j in entradas:
        if j <= 500:
            menores.append(j)
    print(menores)
    print('#' * 10)
