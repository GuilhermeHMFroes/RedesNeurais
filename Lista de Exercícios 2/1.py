import numpy as np

if __name__ == '__main__':

    tam = int(input('Digite um número inteiro: '))

    rt = 0
    for i in range(1, tam + 1):
        #print(i)
        rt = ((6 / (i + 1) ** 2) ** (1/2)) + rt

    print(f'\nResultado:{rt}')
