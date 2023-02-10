# coding: utf-8
# PRACTICE USING LECTURE MATERIAL
ano = 1989
nome = "Luke Skywalker"
saldo = 50
print("Ano: {}, Nome: {}, Saldo: R${:.1f}".format(ano, nome, saldo))
print("O tipo da variável ano é {}".format(type(ano)))
print("O tipo da variável nome é {}".format(type(nome)))
print("O tipo da variável saldo é {}".format(type(saldo)))

# 09FEV • AULA02
# NÃO EXISTE MATRIZ NO PYTHON
# porque não existe tamanho fixo na linguagem
# https://numpy.org/
# interpolação (format, f-string, %)

# SLICE <~~~
nomes = [ 'a', 'b', 'c', 'd' ]
print(nomes[ 1: ]) 				# ‘b’, ‘c’, ‘d’
print(nomes[ 1:-1 ]) 				# ‘b’, ‘c’
nomes.append('e')		# ‘a’, ‘b’, ‘c’, ‘d’, ‘e’

import time
# FOR <~~~
for item in nomes:
    time.sleep(1)
    print(item)

# RANGE <~~~
for number in range(10):
    time.sleep(0.5)
    print(number)

# WHILE <~~~
