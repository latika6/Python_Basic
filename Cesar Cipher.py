# should_continue = True
# while should_continue():
#     alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#     direction = input().lower()
#     text = input().lower()
#     shift = int(input())
#     ceasar(original_text=text, shift_amount=shift, encode_or_decode=direction)
#     restart = input("Yes or No").lower()

#     if restart == "no":
#         should_continue = False
#         print("GoodBye")

# def encrypt(original_text, shift_amount):
#     cipher_text_first = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amount
#         shifted_position = shifted_position % len(alphabet)
#         cipher_text_first+= alphabet[shifted_position]
#     print(cipher_text_first)
# encrypt(original_text=text, shift_amount=shift)

# def decrypt(original_text, shift_amount):
#     cipher_text_second = ""
#     for letter in original_text:
#         shifted_decrypt_position = alphabet.index(letter) - shift_amount
#         shifted_decrypt_position = shifted_decrypt_position % len(alphabet)
#         cipher_text_second += alphabet[shifted_decrypt_position]
#     print(cipher_text_second)
# decrypt(original_text=text, shift_amount=shift)

# def ceasar(original_text, shift_amount, encode_or_decode):
#     cipher_text_second = ""
#     if encode_or_decode == "decode":
#                 shift_amount *= -1
#     for letter in original_text:
#         if letter not in alphabet:
#             cipher_text_second+=letter
#         else:
#             shifted_decrypt_position = alphabet.index(letter) + shift_amount
#             shifted_decrypt_position = shifted_decrypt_position % len(alphabet)
#             cipher_text_second += alphabet[shifted_decrypt_position]
#     print(cipher_text_second)
# ceasar(original_text = text, shift_amount = shift, encode_or_decode =direction)


# Define the Caesar cipher function
def ceasar(original_text, shift_amount, encode_or_decode):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    cipher_text_second = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            cipher_text_second += letter
        else:
            shifted_decrypt_position = alphabet.index(letter) + shift_amount
            shifted_decrypt_position = shifted_decrypt_position % len(alphabet)
            cipher_text_second += alphabet[shifted_decrypt_position]
    print(cipher_text_second)

# Main loop to continue or stop based on user input
should_continue = True
while should_continue:
    # Take inputs from the user
    direction = input("Type 'encode' to encrypt, 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    # Call the Caesar cipher function
    ceasar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    
    # Ask the user if they want to restart or exit
    restart = input("Do you want to go again? Type 'yes' or 'no':\n").lower()
    
    if restart == "no":
        should_continue = False
        print("Goodbye")
