from faker import Faker

fake = Faker('pt-br')

print(fake.name())

for i in range(10):
    print(f'{fake.cpf()} - {fake.name()} ({fake.postcode()})')
