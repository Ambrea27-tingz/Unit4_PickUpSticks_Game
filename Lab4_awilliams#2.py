"""Name: Ambrea Williams
   
   Date: 06/07/2025

   Unit 3: Lab 3

   Description: Guess The Number / Hangman Game. A program that asks the player to guess a random number between 1 and 15. 
   If the guess is incorrect, the next body part is added to the hangman.  
   """

"""The maximum number of incorrect guesses allowed before the game is lost."""
max_sticks = 4

"""The minimum number of incorrect guesses allowed before the game is lost."""
min_sticks = 1 
   
total_stciks = 13

"""Initialize game variables"""
sticks_left = total_stciks
current_player = 1

"""Game instructions"""
print('Welcome to Pick up Sticks!')
print(f'Players take turns picking between {min_sticks} and {max_sticks} sticks.')
print('The player who takes the last stick wins.')
print(f'Total sticks in the pile: {total_stciks}\n')