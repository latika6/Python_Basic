# Write a program to calculate the sum of each column
# type your code here
import numpy as np
A = [
    [1, 4, 8], 
    [5, 7, 3], 
    [9, 14, 2]
    ]

array = np.array(A)
d = np.sum(A)
d

b = np.sum(A, axis=0)
b # column wise

c = np.sum(A, axis=1)
c #row wise