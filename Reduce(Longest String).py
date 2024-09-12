def longest_string(lst):
  return reduce(lambda x, y: x if len(x)>len(y) else y, lst)

print(longest_string(["abc", "xyyz", "bndha"]))
