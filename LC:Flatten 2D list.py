# Flatten a 2D list
def flatten_list(lst):
  return [item for sublist in lst for item in sublist]

print(flatten_list([[1, 2], [3, 4], [5, 6]]))
