import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Create matrix bi-dimensional with M-rows and N-column
M = 10 #rows_qtt
N = 10 #columns_qtt

# Create a empty matrix
matrix = np.empty(shape=(M,N), dtype=int)

x = 3 # exponential
n_start = -10 # range starting from
n_end = 10 # range ending from

# Filling the matrix with quadratic fuction
for i in range(n_start, n_end):
    for j in range(n_start, n_end):
        matrix[i][j] = j**x + 4*i + i*j # Quadractic function for fill the matrix with

print(matrix)

"""
    [Option 1] Plotting the matrix as a 3d graph
"""

# Create a dataframe from the matrix
df = pd.DataFrame(matrix)
print(df)

# Define the XYZ axis
x = df.columns
y = df.index
X, Y = np.meshgrid(x, y)
#Z = df
Z = X + Y

# Plotando Gráfico

fig = plt.figure(figsize=(15,7))

ax = fig.add_subplot(projection = '3d')
ax.plot_surface(X, Y, Z, cmap = 'viridis')

#print(f'\n\nMatrizes:\nx:{X}\n\ny:{Y}\n\nz:{Z}')

plt.show()


