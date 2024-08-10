# Write a code to get the element-wise remainder of an array after division by 8 
# type your code here
import numpy as np
num = [42, 87, 90, 14, 32, 75, 61, 80, 92]
array_num = np.array(num)
array_num % 8

# or

num = [42, 87, 90, 14, 32, 75, 61, 80, 92]
array_num = np.array(num)
remainder_array = np.remainder(array_num, 8)
remainder_array

# or

num = [42, 87, 90, 14, 32, 75, 61, 80, 92]
array_num = np.array(num)
np.mod(array_num, 8)