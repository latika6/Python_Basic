# Love Calculator
# 💪 This is a difficult challenge! 💪 
# You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people: 
# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   
# 2. Then check for the number of times the letters in the word LOVE occurs.   
# 3. Then combine these numbers to make a 2 digit number and print it out. 
# e.g.
# name1 = "Angela Yu" name2 = "Jack Bauer"
# T occurs 0 times 
# R occurs 1 time 
# U occurs 2 times 
# E occurs 2 times 
# Total = 5 
# L occurs 1 time 
# O occurs 0 times 
# V occurs 0 times 
# E occurs 2 times 
# Total = 3 
# Love Score = 53


def calculate_love_score(name1, name2):
    combine_name1 = name1.replace(" ", "")
    combine_name2 = name2.replace(" ", "")
    combined_names = combine_name1 + combine_name2
    lower_names = combined_names.lower()
    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e
    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    second_digit = l + o + v
    score = int(str(first_digit) + str(second_digit))
    return score
love_score = calculate_love_score("Kanye West", "Kim Kardashian")
print(love_score)