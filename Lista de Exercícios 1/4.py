"""

Exercício 4

Faça o gráfico do exemplo anterior utilizando agora a função f(x) = x3 + x2 + x + 3.

"""

from sympy import *
from sympy.plotting import *

if __name__ == '__main__':

    x = Symbol('x')

    # f(x) = x³ + x² + x + 3
    plot(x ** 3 + x ** 2 + x + 3, (x, -10, 10))
