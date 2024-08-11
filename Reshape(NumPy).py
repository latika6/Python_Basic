# Create a 2D numpy array from a 1D array of 20 elements of your choice. 
# Further, subset the first 5 elements from the second element of a resulting 2D array 

# type your code here
import numpy as np
arr_1d = np.arange(1,21)
arr_1d
arr_2d = arr_1d.reshape(2,10)
arr_2d
arr_2d[1][0:5]


