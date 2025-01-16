'''
import random

num_dice = int(input("How many dice would you like to role? "))
sides = int(input("How many sides does the dice have? "))

results = ""
value = 0

for i in range(num_dice):
    random_int = random.randint(1,sides)
    if i == num_dice - 1:
        results += str(random_int)
    else:
        results += str(random_int) + " "
    value += random_int

print("The results were",results)
print("Total is",str(value)) '''

# Remember the Word 7 
# 
# Clears the terminal window and displays header when needed
# Reads instructions from file and displays them.
# Displays 4 words with a 2 second pause between them.
# Prompts user to recall one of those four words. 
# The user is then provided conditional feedback on their response.
# This version read words from a file and selects a subset of 4 words and 
# a correct word randomly.
# (Still violates a number of Software Quality Requirements -to be fixed later)
import time, os, random

# determine the clear command of the current OS
if os.name == 'nt': # nt is the internal name of the MS Windows OS
    clear_command = 'cls'
else:
    clear_command = 'clear'
    

# clear screen & display the header
os.system(clear_command)
header_line = '-' * 80
header_content = ' Remember the Word'
print(header_line)     
print(header_content)
print(header_line)

# display instructions
filename = 'classroom_instructions.txt'
mode = 'r'
instructions_file = open(filename, mode)
instructions = instructions_file.read()
instructions_file.close()
print(instructions)

# prompt the player to continue
input('Press enter key to display the words')


# display a series of randomized words, one at a time, with a pause between them, words must have different starting letters, cleare the screen and displaying the header in-between
words_file = open('classroom_words.txt', 'r')
all_words_str = words_file.read()
words_file.close()
all_words = all_words_str.splitlines()
words_to_display = random.sample(all_words, 4)
correct_word = random.choice(words_to_display)
start_letter = correct_word[0]
for word in words_to_display:
    # clear screen & display the header
    os.system(clear_command)
    print(header_line)     
    print(header_content)
    print(header_line)
    print(word)
    time.sleep(2)

# prompt the player for a word that starts with a particular letter
# assume the correct word is chair
# clear screen & display the header
os.system(clear_command)
print(header_line)     
print(header_content)
print(header_line)
guess = input('Which word started with the letter ' + start_letter + '? ')

# display feeback
# clear screen & display the header
os.system(clear_command)
print(header_line)     
print(header_content)
print(header_line)
print('The answer was ' + correct_word + '.')
print('You guessed ' + guess + '.') # Alternative: print('You guessed', guess)
if guess == correct_word:
    print('Congratulations, you are correct.')
else:
    print('Sorry, your guess is incorrect')
    

# prompt player to continue or not


