# Remove Punctuation from a String
import string
s = "Hello!!!, he said ---and went."
translator = str.maketrans('', '', string.punctuation)
s = s.translate(translator)
print(f"String after removing punctuation: {s}")
