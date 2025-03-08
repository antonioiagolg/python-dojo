'''
Number guessing game. 
The game calculates the number of minimum guesses based on the range the user
defines to choose the mistery number. The formula is:
log2(max_range - min_range + 1)
Based on the number of guesses, the player will try to find the mistery number.
The game will say if the guess is too high or too low, giving a hint to the player
for the next guess.

References:
- https://www.geeksforgeeks.org/number-guessing-game-in-python/

Explored here:
- random lib
- math lib
- control flow statements
'''

import random
import math


print("Configuring the game...")
min = int(input("Please set the minimum number: "))
max = int(input("PLease set the maximum number: "))

# Initializing the game variables
number_guesses = 1
mistery_number = random.choice(range(min,max))
minimun_guesses = math.ceil(math.log2(max - (min + 1)))

print("Let's play!")
print(f"You have {minimun_guesses} guesses to use.")
while True:
    guess = int(input("Make your guess: "))
    if guess == mistery_number:
        print(f"Congratulations! You found the number after {number_guesses} guess(es)")
        break

    if number_guesses > minimun_guesses:
        print("Game over! Better luck next time")

    if guess > mistery_number:
        print("Try again! You guessed to high!")
    else:
        print("Try again! You guessed to low!")

    number_guesses += 1
    
