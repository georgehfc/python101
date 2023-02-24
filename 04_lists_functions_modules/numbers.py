# Valores fora de ordem
valores = [1, 7, 7, 19, 3, 2, 11, 15, 6, 1, 5]

# Exibição da lista
print("A lista foi criada assim: {}".format(valores))

# Contagem de elementos
contagem = valores.count(7)
print(f"Nessa lista o número 7 aparece {contagem} vezes")

# Invertendo a lista
valores.reverse()
print(f"A lista agora está invertida: {valores}")

# Ordenando a lista
valores.sort()
print(f"A lista agora está ordenada: {valores}")

# Tamanho da lista
tamanho = len(valores)
print(f"A lista tem {tamanho} elementos")

# Soma dos elementos
soma = sum(valores)
print(f"A soma dos elementos é {soma}")
