# coding: utf-8
# 20. Usando funções, faça um programa que simule um hotel de animais, onde tem
# vaga para 10 cachorros, 5 gatos e 8 capivaras. Peça o nome do animal e qual
# animal é, e retorne se é possível hospedar o animal ou não. Se for possível
# hospedar, guarde o nome do animal e qual animal é. Se não for possível
# hospedar, diga "não é possível hospedar"

MAX_DOG = 10
MAX_CAT = 5
MAX_CAPYBARA = 8

petshop = {
    'dog': [],
    'cat': [],
    'capybara': []
}

def display(animal):
    print(f"\n{len(petshop[animal])} {animal}s")
    for hospede in petshop[animal]:
        print(f"# {hospede}")

def get_max(animal):
    if animal == 'dog':
        return MAX_DOG
    elif animal == 'gato':
        return MAX_CAT
    else:
        return MAX_CAPYBARA

control = 1
while control != 0:
    if control == 3:
        print("\n--- OUR PET GUESTS ---")
        display('dog')
        display('cat')
        display('capybara')
        print('\n' + '#' * 10)

    elif control == 2:
        pet_name = input("What's the pet name? ")
        animal = input("What kind of animal is it? ").lower()

        if petshop[animal].count(pet_name):
            for i in range(len(petshop[animal])):
                if petshop[animal][i] == pet_name:
                    print(f"Removing {pet_name}... Removed!")
                    petshop[animal].pop(i)
            print(f"Now we have {len(petshop[animal])} {animal}s in the house.")
        else:
            print(f"We have {len(petshop[animal])} {animal}s in the house, none with such name.")

    else:
        pet_name = input("What's the pet name? ")
        animal = input("What kind of animal is it? ").lower()

        if petshop.get(animal) == None:
            print(f"We don't host {animal}s")
        else:
            if len(petshop[animal]) >= get_max(animal):
                print(f"We can't host {pet_name} now... :(")
            else:
                petshop[animal].append(pet_name)
                print(f"Sure, let's host {pet_name}. Done!")

    print("Try again?")
    control = int(input("\n# 0 EXIT # 1 HOST # 2 REMOVE # 3 PRINT >>> "))

print("Bye!")
