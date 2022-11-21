"""

Exercício 5

Dado um vetor com 10 valores, escreva as funções que calculam a média e o desvio padrão desse vetor.
Compare os resultados de suas funções com os resultados obtidos pelas funções mean e sd.

"""

import numpy as np

def Media(vet):

    media = np.sum(vet)/len(vet)
    print(f'Média: {media}')
    return media

def DesvioPadrao(vet):

    media = Media(vet)

    varianca = 0
    for i in range(len(vet)):
        varianca = (vet[i] - media)**2 + varianca
    varianca = varianca / len(vet)

    desvioPadrao = varianca**1/2

    print(f'Desvio padrão: {desvioPadrao}')

if '__main__':

    tamVet = 10
    vet = np.random.randint(1, 99, size=(tamVet))
    #vet = [3, 7, 6, 5, 4]
    print(f'Vetor: {vet}')

    DesvioPadrao(vet)
