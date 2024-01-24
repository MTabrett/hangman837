import random

word_list = ["grape", "grapefruit", "gooseberry", "lychee", "blueberry"]

class Hangman:
    def __init__(self, word_list, num_lives:int=5):
        # Pick a random word from the word list
        self.word = random.choice(word_list)
        # Create a list of underscores for each letter in the word
        self.word_guessed = ["_" for _ in self.word]
        # Count the number of unique letters in the word
        self.num_letters = len(set(self.word))
        # Set the number of lives to the given parameter
        self.num_lives = num_lives
        # Set the word list to the given parameter
        self.word_list = word_list
        # Create an empty list for the guesses
        self.list_of_guesses = []
    
    # Define the check_guess method
    def check_guess(self, guess):

        # Convert the guessed letter to lower case
        guess = guess.lower()

        # Create an if statement that checks if the guess is in the word
        if guess in self.word:

            # Print a message saying "Good guess! {guess} is in the word."
            print(f"Good guess! {guess} is in the word.")

            # Loop through the word and the word_guessed lists
            for i in range(len(self.word)):

                # If the letter in the word matches the guess
                if self.word[i] == guess:

                    # Replace the underscore with the letter in the word_guessed list
                    self.word_guessed[i] = guess

                    # Decrement the num_letters count by one
                    self.num_letters -= 1
         # Create an else block for when the guess is not in the word
        else:

            # Decrement the num_lives count by one
            self.num_lives -= 1

            # Print a message saying, "Sorry, {guess} is not in the word."
            print(f"Sorry, {guess} is not in the word.")

            # Print a message saying, "You have {num_lives} lives left."
            print(f"You have {self.num_lives} lives left.")

    # Define the ask_for_input method
    def ask_for_input(self):

        # Create a while loop and set the condition to True
        while True:

            # Ask the user to guess a letter and assign this to a variable called guess
            guess = input("Guess a letter: ")

            # Create an if statement that runs if the guess is NOT a single alphabetical character
            if len(guess) != 1 or not guess.isalpha():

                # Print a message saying "Invalid letter. Please, enter a single alphabetical character."
                print("Invalid letter. Please, enter a single alphabetical character.")

            # Create an elif statement that checks if the guess is already in the list_of_guesses
            elif guess in self.list_of_guesses:

                # Print a message saying, "You already tried that letter!"
                print("You already tried that letter!")

            # If the guess is a single alphabetical character and it's not already in the list_of_guesses, create an else block
            else:

                # Call the check_guess method. Remember to pass the guess as an argument to this method.
                self.check_guess(guess)

                # Append the guess to the list_of_guesses
                self.list_of_guesses.append(guess)
                print(guess)
                # Break out of the loop
                break

# Create an instance of the Hangman class
play_game = Hangman(word_list)

# Call the ask_for_input method.
play_game.ask_for_input()