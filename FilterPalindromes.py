# Filter palindromes
def is_pallindrome(s):
  return s == s[::-1]

def filter_pallindrome(lst):
  return list(filter(is_pallindrome, lst))

print(filter_pallindrome(["level", "world", "radar", "python"]))
