# Need to import "Random" package to use "Choice" method to randomly pick a word.
import random

# Create a list containing the names of my 5 favourite fruits.
available_word_list = ["grape", "grapefruit", "gooseberry", "lychee", "blueberry"]

# # Assign the list to a variable called word_list.
# word_list = fruits

# Print the contents of word_list.
# print(available_word_list)

# Use the random.choice method to pick a random word from the list.
random_selected_word = random.choice(available_word_list)

# Print out the word to the standard output to check random choice works.
# print(random_selected_word)

# Using the input function, ask for entry of a single letter.
player_guess = input("Please enter a single letter: ")

# # Assign the user input to a variable called guess.
# guess = letter

# Create an if statement that checks if the length of the input is equal to 1 and the input is alphabetical.
if len(player_guess) == 1 and player_guess.isalpha():
  
  # In the body of the if statement, print a message that says, "Good guess!".
  print("Good guess!")

# Create an else block that prints "Oops! That is not a valid input." if the preceding conditions are not met.
else:
  print("Oops! That is not a valid input.")

