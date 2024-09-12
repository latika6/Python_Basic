def filter_odd_numbers(lst):
  return list(filter(lambda x: x%2!=0, lst))
print(filter_odd_numbers([1, 2, 3, 4, 5, 6, 7]))
