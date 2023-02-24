# Feb16
# A FUNCTION
def soma(x, y):
    return x + y
# CALLING FUNCTION
print(soma(41, 1))

# CRIAR FUNÇÃO QUE RECEBE UM NOME E DEVOLVE A FRASE
# "Boa noite, {nome}" E depois usar essa função e
# imprimir na tela
def saudacao(nome):
    return "Boa noite, {}".format(nome) # MÁ PRÁTICA INPUT() DENTRO DE FUNÇÃO
# FUNÇÕES DEVEM, QUASE SEMPRE, RECEBER E RETORNAR VALORES E SÓ
print(saudacao("George"))
