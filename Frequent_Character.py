# Find the Most Frequent Character
from collections import Counter
def most_freq_char(string):
    string = string.strip().lower()
    char_counts = Counter(string)
    most_freq = max(char_counts, key=char_counts.get)
    return most_freq

string = "Latika"
print(most_freq_char(string))
