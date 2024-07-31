#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# ================================================
# password = []
# for i1 in letters:
#     random_i1 = random.choice(letters)
#     password.append(random_i1)
# for i2 in letters:
#     random_i2 = random.choice(letters)
#     password.append(random_i2)
# for i3 in letters:
#     random_i3 = random.choice(letters)
#     password.append(random_i3)
# for i4 in letters:
#     random_i4 = random.choice(letters)
#     password.append(random_i4)
# for n1 in numbers:
#     random_n1 = random.choice(numbers)
#     password.append(random_n1)
# for n2 in numbers:
#     random_n2 = random.choice(numbers)
#     password.append(random_n2)
# for s1 in symbols:
#     random_s1 = random.choice(symbols)
#     password.append(random_s1)
# for s2 in symbols:
#     random_s2 = random.choice(symbols)
#     password.append(random_s2)
# print(password)

# ====================================================

easy_password = []
for let in range(1, nr_letters+1):
    easy_password.append(random.choice(letters))
for sym in range(1, nr_symbols+1):
    easy_password.append(random.choice(symbols))
for numb in range(1, nr_numbers+1):
    easy_password.append(random.choice(numbers))

print("Easy Level Password:", "".join(easy_password))

# =====================================================
# Hard Level - Order of characters randomized:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
hard_password = easy_password.copy()
random.shuffle(hard_password)

print("Hard Level Password:", "".join(hard_password))
