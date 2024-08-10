# type your code here
weights = [74.2, 85, 74, 67.9, 52, 70.5, 86, 51.8, 64, 82]
array_weight = np.array(weights)
for weight in array_weight:
    if weight>68:
        print(weight)


# but i need to convert into 1D array

weights = [74.2, 85, 74, 67.9, 52, 70.5, 86, 51.8, 64, 82]
array_weight = np.array(weights)
mask = array_weight > 68
array_weight[mask]
