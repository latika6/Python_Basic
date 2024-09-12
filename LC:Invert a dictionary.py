# Invert a dictionary
def inv_dict(d):
  return {v:k for k, v in d.items()}

print(inv_dict({'a': 1, 'b': 2, 'c': 3}))
