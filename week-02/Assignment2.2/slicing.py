import numpy as np

# Create a 6x4 matrix with random integer values between 20 and 85
matrix = np.random.randint(low=20, high=85, size=(6,4))

# Print the initial matrix
print(f'Inital Matrix: \n\n {matrix}')

# Add a new row at index 4 that is the sum of rows 0 and 2
matrix[4] = np.sum( matrix[[0,2], :], axis=0)

# Add a new row at index 5 that is the sum of rows 1 and 3
matrix[5] = np.sum( matrix[[1,3], :], axis=0)

# Print the modified matrix
print(f'\nMatrix After Slicing: \n\n {matrix}')


