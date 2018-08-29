import matplotlib.pyplot as plt
import numpy as np

from generate_grid import generate_starting_grid
from plot_current_grid import plot_current_grid

print("Empty grid:")
grid=np.zeros((10,10))
fig = plt.matshow(grid)
plt.colorbar()
plt.show()
# print("Add ships:")
# ships=[[1,2,0],[1,3,1],[1,4,1],[3,4,1],[3,5,1],[3,6,1],[6,2,1],[6,3,1],[6,4,1]]
#
out_grid=plot_current_grid(grid, generate_starting_grid())