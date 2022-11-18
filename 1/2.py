import numpy as np
import matplotlib.pyplot as plt

x, y = np.mgrid[-1:1:500J,-1:1:500J]

z = x + y

fig = plt.figure(figsize=(15,7))

ax = fig.add_subplot(projection = '3d')
ax.plot_surface(x, y, z, cmap = 'viridis')

print(f'x:{x}\n\ny:{y}\n\nz:{z}')

#plt.show()