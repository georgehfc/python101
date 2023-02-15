# coding: utf-8
# 16. Usando o programa criado no exercício 15, crie uma lista de funcionários.
# Você deve pedir os dados, até que o nome digitado seja "0" (o número zero).
# Ao terminar de cadastrar todos os funcionários, mostre a lista
controle = 1
funcionarios = []

while controle != 0:
    func_nome = input("Nome: ")
    func_cargo = input("Cargo: ")
    func_inscricao = int(input("Inscrição: "))

    funcionarios.append(
        {'nome': func_nome,
        'cargo': func_cargo,
        'inscricao': func_inscricao}
    )

    controle = int(input("Mais um funcionário? Digite 0 para sair. "))

print('#' * 20)
for funcionario in funcionarios:
    for k, v in funcionario.items():
        print(f"{k}: {v}")
    print('*' * 5)
print('#' * 20)
