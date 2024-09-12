# Find the sum of squares of even numbers
def sum_sqaures_even(lst):
  return (reduce(lambda x, y: x+y, map(lambda x: x**2, filter(lambda x: x%2 !=0, lst))))

print(sum_sqaures_even([1,2,3,4,5]))
