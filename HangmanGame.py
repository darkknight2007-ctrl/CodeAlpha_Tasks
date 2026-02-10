# Hangman_Game(TASK-1)
import random 

# ASCII art representations of the 'Hang-man'
hangman_art = {0: [' ', ' ', ' '],
               1: [' o ', '  ', '  '],
               2: [' o ', ' | ', '  '],
               3: [' o ', '/|', '  '],
               4: [' o ', '/|\\', '  '],
               5: [' o ', '/|\\', '/'],
               6: [' o ', '/|\\', '/ \\']}


def main():
    words = ['mississippi', 'banana', 'orange', 'triangle', 'volcano']
    is_running = True

    print("Welcome to the Hangman Game")
    print("Guess the word correctly to win the game")
    print("*" * 20)

    c = 0  # counter
    n = random.choice(words)  # Target word
    h = ['_'] * len(n)  # Hidden word display
    guessed_letters = []  # list to track all previous attempts

    print('Hint: ' + ' '.join(h))

    while is_running:
        print(f"Letters guessed so far: {', '.join(guessed_letters)}")
        print("HANGMAN:")
        display_man(c)
        print("*" * 20)

        g = input("Enter a letter (press q to quit): ").lower().strip()

        # 1. Handle Quit immediately
        if g == 'q':
            print("Thank you for playing")
            is_running = False
            continue #to prevent ghost logic(not necessary in this case) for safety

        # 2. Validation: Ensure input is exactly one letter
        if len(g) != 1 or not g.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        # 3. Check for duplicate inputs
        if g in guessed_letters:
            print(f"You already guessed '{g}'! Try a different letter.")
            continue

        # Add current guess to the history list
        guessed_letters.append(g)

        # 4. Check if guess is wrong
        if not g in n:
            c += 1
            print(f"Sorry, '{g}' is not in the word.")
        else:
            # Reveal correct letters
            for i in range(len(n)):
                if n[i] == g:
                    h[i] = g
            print('Progress: ' + ' '.join(h))

        # 5. Check Win Condition
        if ''.join(h) == n:
            print("YOU WON!")
            print("The word was: " + n)
            is_running = False

        # 6. Check Loss Condition
        elif c >= 6:
            print("HANGMAN: ")
            display_man(6)
            print("YOU LOSE!")
            print("The word was: " + n)
            is_running = False


def display_man(c):
    #Prints the ASCII art corresponding to the number of mistakes.
    for i in hangman_art[c]:
        print(i)


if __name__ == '__main__':
    main()
