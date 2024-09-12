from functools import reduce

def num_multiply(lst):
  return reduce(lambda x, y: x*y, lst)

print(num_multiply([1,2,3,4]))
