word_list = ["siddharth", "gandharva", "lakshay"]

import random

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
end_of_game = False

print(f'the chosen word is {chosen_word}')

display = []
for _ in range(word_length):
    display += "_"

print(display)   

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess

    print(display)

    if "_" not in display:
        end_of_game = True
        print("You Win!")