# https://docs.python.org/pt-br/3/library/
from matematica import soma
from math import pi
import lecture
import datetime
# from datetime import datetime as dt

print(soma(70, 74))
# print(matematica.subt(10, 2))
print(pi)

estudante = lecture.Estudante(nome='George', documento='123', matricula='4425782')
print(estudante.mostrar_nome_tres_vezes())

hoje = datetime.datetime.now()
print(f'Data e hora: {hoje}')
print(type(hoje))

data = hoje.date()
print(f'Somente data: {data}')
print(type(data))
print(data.weekday)
