# coding: utf-8
# 10. Altere o programa do exercício 07, verificando se o valor do produto é maior
# que zero e se a quantidade de itens é maior que zero. Caso seja zero, mostre uma
# mensagem de erro e peça o valor novamente, até o valor ser digitado corretamente
product_name = input("Qual o nome do produto? ")
product_price = int(input("Qual o preço unitário? "))
while product_price < 0:
    print("Atenção! Não aceitamos números negativos")
    product_price = int(input("Qual o preço unitário? "))
product_amount = int(input("Quantos itens comprados? "))
while product_amount < 0:
    print("Atenção! Não aceitamos números negativos")
    product_amount = int(input("Quantos itens comprados? "))
print("O total a pagar por {} é R${}".format(product_name, product_price * product_amount))
