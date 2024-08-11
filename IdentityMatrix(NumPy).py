# Create an identity matrix with n dimensions (take input from the user). 
# Fill the diagonals of that matrix with the multiples of the number provided by the user; 
# take another input from the user. Consider the output below as an example

import numpy as np
n = 6
multiple = 3
identity_matrix = np.identity(n)
for i in range(n):
    identity_matrix[i, i] = multiple * (i + 1)
print(identity_matrix)