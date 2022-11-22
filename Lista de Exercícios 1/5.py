"""

Exercício 5

Dado um vetor com 10 valores, escreva as funções que calculam a média e o desvio padrão desse vetor.
Compare os resultados de suas funções com os resultados obtidos pelas funções mean e std.

"""

import numpy as np

def Media(vet):

    media = np.sum(vet)/len(vet)
    print(f'Média: {media}')
    return media

def DesvioPadrao(vet):
    '''

    Fórmula desvio padrão populacional: O = (Somatório(x - média)²/n) ** 1/2

    '''

    media = Media(vet)

    somatorio = 0
    for i in range(len(vet)):
        somatorio = ((vet[i] - media) ** 2) + somatorio
        a = ((vet[i] - media) ** 2)

    desvioPadrao = (somatorio / len(vet)) ** (1 / 2)

    print(f'Desvio padrão: {desvioPadrao}\n')

if '__main__':

    tamVet = 10
    vet = np.random.randint(1, 99, size=(tamVet))
    print('=' * 50, '\n\t\t\t\t\tVetor')
    print('=' * 50)
    print(f'Vetor: {vet}\n')

    print('='*50, '\n\t\t\tResultado das minhas funções')
    print('='*50)
    DesvioPadrao(vet)

    print('=' * 50, '\n\t\tResultado das funções mean e std')
    print('=' * 50)
    md = np.mean(vet)
    print(f'mean: {md}')
    dP = np.std(vet)
    print(f'std: {dP}\n')
    print('=' * 50)
