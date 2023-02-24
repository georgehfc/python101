# 09FEV • AULA03
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
