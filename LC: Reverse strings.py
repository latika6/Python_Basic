# Reverse strings in a list
def reverse_string(lst):
  return [s[::-1] for s in lst]

print(reverse_string(["apple", "banana", "pear"]))
