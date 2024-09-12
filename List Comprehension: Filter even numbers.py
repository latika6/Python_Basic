# List Comprehension: Filter even numbers
def filter_even(lst):
  return [x for x in lst if x%2==0]

print(filter_even([1,2, 3 , 4, 5, 6, 7]))
