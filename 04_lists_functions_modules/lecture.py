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

############## DEFINITION

# Função que calcula a velocidade média
def calcularVelocidadeMedia():
    # Solicitar distância e tempo
    distancia = float(input("Digite a distância percorrida"))
    tempo = float(input("Digite o tempo da viagem"))
    # Calcular a velocidade média
    velocidade_media = distancia/tempo
    # Exibir o resultado
    print("A velocidade média é {} km/h".format(velocidade_media))

calcularVelocidadeMedia()

############## RETURN

# Função que calcula a velocidade média
def calcularVelocidadeMedia(distancia, tempo):
    # Calcular a velocidade média
    velocidade_media = distancia/tempo
    # Exibir o resultado
    return velocidade_media

dist = float(input("Informe a distância"))
temp = float(input("Informe o tempo"))

# Chamando a função com valores definidos pelo usuário
print(f"A velocidade media é {calcularVelocidadeMedia(dist, temp)}")
