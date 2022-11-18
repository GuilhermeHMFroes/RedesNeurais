'''

Gerar 2 vetores

 - Altura masc/fem
   Vetor tam: 100
	 - masc centralide 1.8
      - fem centralizde 1.65
 - Peso
	Vetor tam: 100
     - masc 80
     - fem 65

'''

import random
import numpy as np
import matplotlib.pyplot as plt

N = 100

central = 0.5
scale = 0.1

altMasc = np.random.normal(central, scale, N)
'''
for i in range(N):
    a = round(altMasc[i], 2)
    altMasc[i] = a'''

print(altMasc)

#plt.hist(altMasc)
#plt.show()

