import os
import random
import hangman_word
import hangman_art


def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')


# Step 1: Randomly choose a word from the word_list
chosen_word = random.choice(hangman_word.word_list)
display_list = ["_"] * len(chosen_word)
lives = 6
end_of_game = False

# Show 2 random letters at the start
revealed_indices = random.sample(range(len(chosen_word)), 2)
for index in revealed_indices:
    display_list[index] = chosen_word[index]

print(hangman_art.logo)

while not end_of_game:
    clear_screen()
    print(" ".join(display_list))

    guess = input("Guess a letter: ").lower()

    if guess in display_list:
        print(f"You've already guessed '{guess}'. Try a different letter.")
    else:
        if guess in chosen_word:
            for n in range(len(chosen_word)):
                if chosen_word[n] == guess:
                    display_list[n] = guess
            print(f"Good guess! '{guess}' is in the word.")
        else:
            lives -= 1
            print(f"'{guess}' is not in the word. You lost a life.")

    print(hangman_art.stages[lives])

    if "_" not in display_list:
        end_of_game = True
        print("Congratulations! You've won!")

    if lives == 0:
        end_of_game = True
        clear_screen()
        print(hangman_art.stages[lives])
        print(f"You lose. The word was '{chosen_word}'.")
