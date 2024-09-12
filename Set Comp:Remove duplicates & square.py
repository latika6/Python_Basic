# Remove duplicates and square the numbers
def remove_dup_square(lst):
  return {x**2 for x in lst}

print(remove_dup_square([1, 2, 2, 3, 3, 4]))
