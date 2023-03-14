# Crie um programa que calcule e mostre o salário de uma pessoa baseado no valor/hora do
# trabalho e na quantidade de horas trabalhadas, e na quantidade de dias trabalhados
# SCRIPT QUE CALCULA VALOR E HORAS/DIAS DE TRABALHO

# ESCOLHER ENTRE VALOR, HORAS/DIAS OU TOTAL
valor = int(input("Inserir VALOR/hora: "))
horas_trabalhadas = int(input("Inserir HORAS TRABALHADAS: "))
salario = valor*horas_trabalhadas
print(f"Seu SALÁRIO/mês: {salario}€\n...")

controle=1
while controle!=0:
    print("\n####----####")
    print(f"Opções:\n1 • Alterar VALOR\n2 • Alterar HORAS TRABALHADAS\n3 • Alterar SALÁRIO\n" + "*"*12 + "\n0 • SAIR")
    controle = int(input("Escolha: "))

    if controle==1:
        valor = int(input("Alterar VALOR para: "))
        salario = valor*horas_trabalhadas
    elif controle==2:
        horas_trabalhadas = int(input("Alterar HORAS TRABALHADAS para: "))
        salario = valor*horas_trabalhadas
    elif controle==3:
        salario = int(input("Alterar SALÁRIO para: "))

    print(f"$$$$----$$$$\nVALOR/hora: {valor}€/h\nHORAS TRABALHADAS: {horas_trabalhadas}h\nSALÁRIO: {salario}€")
