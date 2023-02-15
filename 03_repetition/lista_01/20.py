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
    nome = input("Qual o nome do hóspede? ")
    especie = input("Que bicho é? ")

    if petshop.get(especie):
        if len(petshop[especie]) > petshop[especie][0]:
            print(f"Não podemos hospedar {nome}... :(")
        else:
            petshop[especie].append(nome)
            print(f"Podemos hospedar {nome}!")
    else:
        print(f"Não hospedamos {especie}s")

    controle = int(input("Tentar novamente? (0 para sair) "))
