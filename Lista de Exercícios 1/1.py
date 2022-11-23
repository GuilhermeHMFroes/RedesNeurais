"""

Exercício 1

Dada uma lista com a nota de cinco alunos, encontre a média, o desvio padrão e ordene as notas.

"""

import random as rd
import numpy as np

if __name__ == '__main__':

    qtAlunos = 5
    ntAlunos = []
    for i in range(qtAlunos):
        ntAlunos.append(round((rd.uniform(0, 10)), 2))

    media = round((np.mean(ntAlunos)), 2)
    desvioPadrao = round((np.std(ntAlunos)), 5)
    ordenado = sorted(ntAlunos)

    print(f'Notas dos alunos: {ntAlunos}\nMédia das notas: {media}\nDesvio Padrão: {desvioPadrao}\nNotas ordenadas: {ordenado}')
