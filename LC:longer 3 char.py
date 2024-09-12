# Filter words longer than 3 characters
def filter_3_words(lst):
  return [x for x in lst if len(x)>3]

print(filter_3_words(["cat", "elephant", "dog", "tiger"]))
