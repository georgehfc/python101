# def operations(n1, n2):
#     print("A soma é: {}".format(n1 + n2))
#     print("A subtração é: {}".format(abs(n1 - n2)))
#     print("A divisão é: {:.1f}".format(max(n1, n2) / min(n1, n2)))
#     print("A multiplicação é: {}".format(n1 * n2))

# x1 = int(input("Digite o primeiro número: "))
# x2 = int(input("Digite o segundo número: "))
# operations(x1, x2)

# Função de soma
def somar(a, b):
    return float(a) + float(b)

# Função de subtração
def subtrair(a, b):
    return float(a) - float(b)

# Função de divisão
def dividir(a, b):
    if b==0:
        return 0
    return float(a) / float(b)

# Função de multiplicar
def multiplicar(a, b):
    return float(a) * float(b)
