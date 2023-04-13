# %%

import numpy as np

matrix = np.random.randint(low=20, high=85, size=(6,4))

print(f'Inital Matrix: \n\n {matrix}')

matrix[4] = np.sum( matrix[[0,2], :], axis=0)
matrix[5] = np.sum( matrix[[1,3], :], axis=0)

print(f'\nMatrix After Slicing: \n\n {matrix}')



