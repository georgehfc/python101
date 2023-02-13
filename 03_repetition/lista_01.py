# coding: utf-8
# 1. Faça um programa que mostre a frase "Estou aprendendo Python!"
print("Estou aprendendo Python!")

# 2. Faça um programa que peça o nome da pessoa e mostre a frase "(pessoa) está
# aprendendo Python!", onde o (pessoa) tem que ser substituído pelo nome da pessoa
name = input("Nome: ")
print("{} está aprendendo Python!".format(name))

# 3. Faça um programa que peça 2 números e mostre o resultado das 4 operacoes entre os dois
# números: soma, subtração, divisão e multiplicação
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
print("A soma é: {}".format(n1 + n2))
print("A subtração é: {}".format(abs(n1 - n2)))
print("A divisão é: {:.1f}".format(max(n1, n2) / min(n1, n2)))
print("A multiplicação é: {}".format(n1 * n2))

# 4. Faça um programa que peça uma frase para a pessoa e mostre a quantidade de
# letras que tem na frase
phrase = input("Digite uma frase e contaremos a quantidade de letras: ")
counter = 0
for letter in phrase:
    if(letter != ' '):
        counter = counter + 1
print("{} letras foram encontradas.".format(counter))

# 5. Faça um programa que peça cinco números e mostre qual o maior e qual o menor
numbers = []
for number in range(5):
    add = int(input("Digite o número {}: ".format(number + 1)))
    numbers.append(add)
print("O maior número é {} e o menor número é {}".format(max(numbers), min(numbers)))

# 6. Faça um programa que peça o nome da pessoa e a idade e diga se a pessoa já
# pode votar, se a pessoa já pode obter a carta de motorista
name = input("Digite o nome da pessoa: ")
age = int(input("Digite a idade da pessoa: "))
if age < 16:
    print("{} ainda n˜åo pode votar e nem obter a carta de motorista". format(name))
else:
    print("{} já pode votar e obter a carta de motorista". format(name))

# 7. Faça um programa que peça o nome de um produto, o valor unitário, a quantidade
# de itens comprados, e mostre o valor total a pagar
product_name = input("Qual o nome do produto? ")
product_price = int(input("Qual o preço unitário? "))
product_amount = int(input("Quantos itens comprados? "))
print("O total a pagar por {} é R${}".format(product_name, product_price * product_amount))

# 8. Faça um script que peça para o usuário digitar um número N e imprima uma
# lista com todos os números de 0 a N-1.
number = int(input("Digite um número: "))
for n in range(number):
    print(n)

# 9. Faça um programa que mostre o nome de dez pessoas (que você já pode deixar
# predefinido) e, pra cada nome, mostre a frase "(pessoa) deve estar aprendendo Python"
names = ['Alexandre', 'Francine', 'Mateus', 'Pablo', 'Erick', 'Danilo', 'Luiz']
for name in names:
    print("{} deve estar aprendendo Python".format(name))

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

# 11. Faça um programa que simule um caixa de supermercado. Você deve entrar com
# o nome do produto, o preço do produto, e a quantidade de unidades compradas. Ao
# final, deve mostrar a lista de produtos, o preço total do produto e o valor total da compra
# Os preços e quantidades devem ser informados com casas decimais
products = []
product = {}
control = 's'
while control.upper() == 'S' or control.upper() == 'SIM':
    product_name = input("Escreva o nome do produto: ")
    product_price = int(input("Qual o preço unitário de {}? ".format(product_name)))
    product_amount = int(input("Quantos {} comprados? ".format(product_name)))
    product = {
        "Name": product_name,
        "Price": product_price,
        "Quantity": product_amount
    }
    products.append(product)
    control = input("Mais um produto? (S - Sim ou N - Não) ")
print("### SUA CONTA ###")
total = 0
for unique_product in products:
    for key, value in unique_product.items():           # .items() IS BUILT-IN
        print(f"{key}: {value}")
        product_subtotal = unique_product["Price"] * unique_product["Quantity"]
    print(f"Subtotal: {product_subtotal}")
    total = total + product_subtotal
    print("*" * 10)
print(f"TOTAL: {total}")
