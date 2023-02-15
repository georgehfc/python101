# coding: utf-8
import datetime
# 17. Crie um programa que define uma função que recebe o ano de nascimento de
# uma pessoa e mostre a idade atual de acordo com o ano atual
print("Hoje é teu aniverseirio, tás de parabuains! 🎉")
ano = int(input("Em que ano você nasceu? "))
mes = int(input("Em que mês você nasceu? "))
dia = int(input("Em que dia você nasceu? "))

from datetime import date
hoje = date.today()
dias_de_vida = (hoje - date(ano, mes, dia)).days
anos_de_vida = hoje.year - ano
print(f"Parabuains! Você tem {anos_de_vida} anos.")
print(f"Ou melhor, você tem {dias_de_vida} dias de vida.")
