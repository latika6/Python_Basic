# Conditional comprehensions
def even_odd(lst):
  return ["even" if x%2==0 else "odd" for x in lst]

print(even_odd([1, 2, 3, 4, 5]))
