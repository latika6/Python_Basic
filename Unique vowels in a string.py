# Unique vowels in a string
def unique_vowels(s):
  vowels = 'aeiou'
  return {char for char in s if char in vowels}

print(unique_vowels('hello world'))
