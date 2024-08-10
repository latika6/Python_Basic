# Write a code to generate 10 random integers between 20 to 40 (Is it possible to generate same random numbers everytime? If yes, describe the function)
# type your code here
import numpy as np
import random
random_number = np.random.randint(20,41,10)
random_number

# if we try to fix the random numbers, we can use seed function
random_number = np.random.seed(seed=12)
random_number = np.random.randint(20,41,10)
random_number
