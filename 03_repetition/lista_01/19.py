# coding: utf-8
# 19. Defina uma função que calcula um desconto em um preço. Para isso ela deve
# receber dois números, o preço inicial e a porcentagem de desconto. A função
# deve retornar o preço com o desconto aplicado
preco = float(input("Preço (R$): "))
desconto = float(input("Desconto (%): ")) / 100

print("Desconto aplicado: R${:.1f}".format(preco - preco * desconto))
