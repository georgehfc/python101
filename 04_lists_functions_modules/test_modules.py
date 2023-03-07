# Library, Package, Module
# Importação do módulo calc.py
import calc

# Solicitando valores ao usuário
valor1 = input("Digite um valor: ")
valor2 = input("Digite outro valor: ")

# Armazenando a soma
soma = calc.somar(valor1, valor2)

# Exibindo a soma
print(f"A soma é {soma}")
