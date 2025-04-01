# Count Vowels in a String
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
s = "hello"
print(f"Number of vowels in the string: {count_vowels(s)}")

or

# Count Vowels in a String
vowels = "aeiou"
string = "Latika"
string.lower()
count = 0
for char in string:
    if char in vowels:
        count +=1
print(count)
