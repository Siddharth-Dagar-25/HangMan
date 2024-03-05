word_list = ["siddharth", "gandharva", "lakshay"]

import random

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

print(f'the chosen word is {chosen_word}')

display = []
for _ in range(word_length):
    display += "_"

print(display)   


guess = input("Guess a letter: ").lower()

for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = guess

print(display)