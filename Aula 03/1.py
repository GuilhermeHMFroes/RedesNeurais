'''

Algorítimo de Regressão Linear

'''

import matplotlib.pyplot as plt
import numpy as np
import random as rd
import seaborn as sns

if __name__ == '__main__':

    qtPontos = 200

    x = np.arange(qtPontos)
    delta = np.random.normal(x, qtPontos, size=qtPontos)
    y = (0.5 * (x ** 2 + 3 * x + 10)) + 10 * delta

    plt.plot(x, y, 'o', color="orange")
    m, b = np.polyfit(x, y, 1)

    plt.plot(x, m*x+b, color="purple")

    plt.show()
