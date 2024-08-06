stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

                                                                    
                                                                    
import random
word_list = ['aardvark', 'baboon', 'camel']
lives = 6
choosen_word = random.choice(word_list)
print(choosen_word)
length_word = len(choosen_word)
for _ in range(1,length_word+1):
    print("_", end=" ")
game_over = False
correct_letter = []
while not game_over:
    user_input = input("Guess a letter: ")
    guess = user_input.lower()
    display = ""
    for letter in choosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(letter)
        elif letter in correct_letter:
            display += letter
        else:
            display += "_"
    
    print(display)

    if guess not in choosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose.")
    
    if "_" not in display:
        game_over = True
        print("You Win.")

    print(stages[lives])