# coding: utf-8
# 20. Usando funções, faça um programa que simule um hotel de animais, onde tem
# vaga para 10 cachorros, 5 gatos e 8 capivaras. Peça o nome do animal e qual
# animal é, e retorne se é possível hospedar o animal ou não. Se for possível
# hospedar, guarde o nome do animal e qual animal é. Se não for possível
# hospedar, diga "não é possível hospedar"

MAX_CACHORRO = 10
MAX_GATO = 5
MAX_CAPIVARA = 8

petshop = {
    'cachorro': [MAX_CACHORRO],
    'gato': [MAX_GATO],
    'capivara': [MAX_CAPIVARA]
}

controle = 1
while controle != 0:
    if controle == 3:
        print(petshop)
    elif controle == 2:
        nome = input("Gostaria de retirar que bicho? ")
        especie = input("Que bicho é? ").lower()

        print(f"Temos {len(petshop[especie]) - 1} {especie}s hospedados")
        for i in range(1, len(petshop[especie])):
            if petshop[especie][i] == nome:
                print(f"Removendo {nome}... Removido!")
                petshop[especie].pop(i)

    else:
        nome = input("Qual o nome do hóspede? ")
        especie = input("Que bicho é? ")

        if petshop.get(especie):
            if len(petshop[especie]) > petshop[especie][0]:
                print(f"Não podemos hospedar {nome}... :(")
            else:
                petshop[especie].append(nome)
                print(f"Podemos hospedar {nome}. Pronto!")
        else:
            print(f"Não hospedamos {especie}s")

    print("Tentar novamente?")
    controle = int(input("# 0 SAIR # 1 HOSPEDAR # 2 RETIRAR # 3 IMPRIMIR >>> "))

print("Saindo...")
