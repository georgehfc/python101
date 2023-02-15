# coding: utf-8
# 11. Faça um programa que simule um caixa de supermercado. Você deve entrar com
# o nome do produto, o preço do produto, e a quantidade de unidades compradas. Ao
# final, deve mostrar a lista de produtos, o preço total do produto e o valor total da compra
# Os preços e quantidades devem ser informados com casas decimais

products = []
product = {}
control = 's'

while control.upper() == 'S' or control.upper() == 'SIM':
    product_name = input("Escreva o nome do produto: ")
    product_price = float(input("Qual o preço unitário de {}? ".format(product_name)))
    product_amount = int(input("Quantos {} comprados? ".format(product_name)))
    product = {
        "Nome": product_name,
        "Preço": product_price,
        "Quantidade": product_amount
    }
    products.append(product)
    control = input("Mais um produto? (S - Sim ou N - Não) ")

print("### SUA CONTA ###")

total = 0

for unique_product in products:
    for key, value in unique_product.items():           # .items() IS BUILT-IN
        print(f"{key}: {value}")
        product_subtotal = unique_product["Preço"] * unique_product["Quantidade"]
    print(f"Subtotal: {product_subtotal}")
    total = total + product_subtotal
    print("*" * 10)

print(f"TOTAL: R${total}")
