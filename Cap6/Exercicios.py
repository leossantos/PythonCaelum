def velocidade_media(distancia, tempo):
    velocidade = divisao(distancia, tempo)
    return velocidade
    pass


def soma(a, b):
    return a + b
    pass


def subtracao(a, b):
    return a - b
    pass


def multiplicacao(a, b):
    return a * b
    pass


def divisao(a, b):
    return a / b
    pass


def calculadora(a, b):
    som = soma(a, b)
    sub = subtracao(a, b)
    mul = multiplicacao(a, b)
    div = divisao(a, b)
    print("Soma: {}; Subtração: {}; Multiplicação: {}; Divisão: {}".format(som, sub, mul, div))


i = 0
while i == 0:
    dist = int(input("Distância: "))
    temp = int(input("Tempo: "))
    vel = velocidade_media(dist, temp)
    print("Velocidade Média:", vel)
    #    soma(dist, temp)
    #    subtracao(dist, temp)
    calculadora(dist, temp)
    i = int(input("Continuar: "))
