# Find the Frequency of Characters in a String
s = "hello"
frequency = {}
for char in s:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1
print(f"Frequency of characters: {frequency}")
