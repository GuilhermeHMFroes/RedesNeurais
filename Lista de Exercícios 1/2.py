"""

Exercício 2

Faça um algoritmo para multiplicar matrizes que sejam compatíveis.

"""

import numpy as np

if __name__ == '__main__':

    mt1 = np.random.randint(1, 99, size=(5, 7))
    mt2 = np.random.randint(1, 99, size=(5, 7))
    mt3 = np.multiply(mt1, mt2)

    print(f'Matriz 1\n{mt1}\n\nMatriz 2\n{mt2}\n\nMatriz resultado\n{mt3}')