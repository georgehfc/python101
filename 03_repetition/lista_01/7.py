# coding: utf-8
# 7. Faça um programa que peça o nome de um produto, o valor unitário, a quantidade
# de itens comprados, e mostre o valor total a pagar
product_name = input("Qual o nome do produto? ")
product_price = int(input("Qual o preço unitário? "))
product_amount = int(input("Quantos itens comprados? "))
print("O total a pagar por {} é R${}".format(product_name, product_price * product_amount))
