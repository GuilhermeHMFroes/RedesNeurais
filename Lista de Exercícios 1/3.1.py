"""

Exercício 3

Escreva uma função para calcular f (x) = x² − 3x + 2.
Atribua uma sêquencia de 20 valores e faça o gráfico (x,y) desta função.

"""

from sympy import *
from sympy.plotting import *

if __name__ == '__main__':

    x = Symbol('x')

    # f(x) = x² − 3x + 2
    plot(x ** 2 - 3 * x + 2, (x, -7, 10))