# Write a program to get the fifth power of the first five positive integers
# type your code here
import numpy as np
import random
first_fifth = np.random.randint(10,20,5)
fifth_array = np.array(first_fifth)
power_number = fifth_array ** 5
power_number

# or 

random_fifth = np.arange(1,6)
random_power = np.power(random_fifth, 5)
random_power

 # Write a program to create an array of all the odd integers from 50 to 100 
arr = np.arange(50,101)
mask = (arr % 2 != 0)
arr[mask]
