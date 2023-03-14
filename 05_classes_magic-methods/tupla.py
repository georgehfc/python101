# Importando o módulo sys para conseguirmos usar o getsizeof
import sys
# Criando uma lista e uma tupla vazias, respectivamente
lista_vazia = []
tupla_vazia = ()
# Printando o tipo e tamanho de cada estrutura
print("O objeto lista_vazia é do tipo {} e ocupa {} bytes na memória".format(type(lista_vazia), sys.getsizeof(lista_vazia)))
print("O objeto tupla_vazia é do tipo {} e ocupa {} bytes na memória".format(type(tupla_vazia), sys.getsizeof(tupla_vazia)))

# Criação de uma tupla com as categorias dos Jedi
categorias = ("Youngling", "Padawan", "Knight", "Master")
# Exibindo cada item da tupla usando um loop
for categoria in categorias:
    print(categoria)
