'''
Word guessing game. The user will input a character and the game
will check if this character is in the mistery world or not, and it 
will display the guessed character and the hidden places. The user has
12 turns to guess the words.

References:
- https://www.geeksforgeeks.org/python-program-for-word-guessing-game/

Explored here:
- random lib
- control flow statements

Here I prefered to use the string concatenation and them print the banner
to show the actual letters guessed, to avoid checking flags and empty print statements.
The user don't need to guess the space char.
'''

import random

guesses = ''
turns = 12
words = ['azure gunvolt strike', 'narita boy', 'tomb raider', 'the elder scrolls skyrim', 'half life', 'far cry', 'teslagrad', 'neon abyss', 'enter into the gungeon', 'ori', 'moonlighter']
mistery_word = random.choice(words)

# greeting the player
player = input("What's is your name? ")
print(f"Good luck, {player}!")

while turns > 0:
    char = input("Guess a character: ")
    if char not in mistery_word:
        turns -= 1
        print(f"Wrong guess, you have {turns} remaining...")
        continue

    if char not in guesses:
        guesses += char
    else:
        print("You already guesses this letter!")

    banner = ''
    for letter in mistery_word:
        if letter in guesses or letter == " ":
            banner += letter
        else:
            banner += "_"

    if "_" not in banner:
        print(f"Congratulations! You found the word {banner}!")
        break
    else:
        print(banner)

if turns == 0:
    print(f"Better luck next time, {player}!")

