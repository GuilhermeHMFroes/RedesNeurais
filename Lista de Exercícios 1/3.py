"""

Exercício 3

Escreva uma função para calcular f (x) = x² − 3x + 2.
Atribua uma sêquencia de 20 valores e faça o gráfico (x,y) desta função.

"""

import numpy as np
import matplotlib.pyplot as plt

def Delta(a, b, c):

    delta = b ** 2 - 4 * a * c

    return delta

def Baskara(a, b, c):

    delta = Delta(a, b, c)

    x1 = (-b + (delta ** 1/2)) / (2 * a)
    x2 = (-b - (delta ** 1 / 2)) / (2 * a)

    Grafico(a, b, c, delta, x1, x2)

def Grafico(a, b, c, x1, x2):

    eixoX = []
    eixoY = []
    zero = []

    variacao = abs(x1 - x2)
    if variacao < 3:
        variacao = 3

    for x in np.arange(x1 - variacao, x2 + variacao, variacao / 100):
        y = a * (x ** 2) + b * (x) + c
        eixoX.append(x)
        eixoY.append(y)
        zero.append(0.0)

    for i in range(len(eixoX)):
        eixoX[i] = round(eixoX[i] , 2)
        eixoY[i] = round(eixoY[i], 2)

    plt.plot(eixoX, eixoY, color="blue")
    plt.plot(eixoX, zero, color="black")
    plt.plot(zero, eixoY, color="black")

    print('='*50)
    print('\t\t\t\tPosições do gráfico')
    print('=' * 50)

    for i in range(len(eixoX)):
        print(f'[{eixoX[i]}, {eixoY[i]}]')

    print('=' * 50)

    plt.show()

if __name__ == '__main__':

    # x² − 3x + 2
    a = 1
    b = -3
    c = 2

    Baskara(a, b, c)