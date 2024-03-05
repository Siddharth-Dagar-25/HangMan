word_list = ["siddharth", "gandharva", "lakshay"]

import random

chosen_word = random.choice(word_list)

print(f'the chosen word is {chosen_word}')

display = []
for _ in range(len(chosen_word)):
    display += "_"

print(display)   
 

guess = input("Guess a letter: ").lower()

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")    