import random
from Hangman_word import *
from Hangman_art import *

# Randomly choose the word to guess
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6
end_of_game = False

print(logo)
print(f"The word to guess is {chosen_word}")

display = []
for char in display:
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You have already guessed {guess}, please choose another letter")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")
    print(stages[lives])
