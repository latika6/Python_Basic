def square_odd_number(lst):
  return list(map(lambda x: x ** 2, filter(lambda x: x%2 !=0, lst)))

print(square_odd_number([1,2,3,4]))
