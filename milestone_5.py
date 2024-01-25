import random

available_word_list = ["grape", "grapefruit", "gooseberry", "lychee", "blueberry"]

# Create Hangman class and initialise the attributes of the class
class Hangman:
    def __init__(self, available_word_list, number_lives_start:int=5):
        self.random_selected_word = random.choice(available_word_list)
        self.word_guessed = ["_" for _ in self.random_selected_word]
        print(*self.word_guessed)
        self.number_letters = len(self.random_selected_word)
        print(f"The mystery word has {self.number_letters} characters")
        self.number_lives = number_lives_start
        self.word_list = available_word_list
        self.list_of_guesses = []
        
        # print(*game.word_guessed)

    # Define the check_guess method
    def check_guess_correct(self, players_guess):

        players_guess = players_guess.lower()

        # Create an if statement that checks if the guess is in the word
        if players_guess in self.random_selected_word:

            print(f"Good guess! {players_guess} is in the word.")

            # Loop through the word and the word_guessed lists to define what happens if the letter is in the word
            for i in range(len(self.random_selected_word)):

                if self.random_selected_word[i] == players_guess:

                    self.word_guessed[i] = players_guess

                    self.number_letters -= 1
         # Create an else block for when the guess is not in the word
        else:

            self.number_lives -= 1

            print(f"Sorry, {players_guess} is not in the word.")

            print(f"You have {self.number_lives} lives left.")

    # Define the ask_for_input method
    def ask_player_for_input(self):

        # Create a while loop and set the condition to True
        while True:

            players_guess = input("Guess a letter: ")

            # Create an if statement that runs if the guess is NOT a single alphabetical character
            if len(players_guess) != 1 or not players_guess.isalpha():

                print("Invalid letter. Please, enter a single alphabetical character.")

            # Create an elif statement that checks if the guess is already in the list_of_guesses
            elif players_guess in self.list_of_guesses:

                print("You already tried that letter!")

            # If the guess is a single alphabetical character and it's not already in the list_of_guesses, create an else block
            else:

                self.check_guess_correct(players_guess)

                self.list_of_guesses.append(players_guess)
                print(players_guess)
                print(*self.word_guessed)
                # Break out of the loop
                break

# Define the play_game function that takes word_list as a parameter
def play_game(word_list):

    number_lives = 5

    game = Hangman(word_list, number_lives)

    while True:

        if game.number_lives == 0:
            print("You lost!")
            break

        # Check if the num_letters is greater than 0
        elif game.number_letters > 0:

            # Call the ask_for_input method
            game.ask_player_for_input()

        # If the num_lives is not 0 and the num_letters is not greater than 0
        else:

            # Print a message saying 'Congratulations. You won the game!'
            print("Congratulations. You won the game!")

            # Break out of the loop
            break

play_game(available_word_list)

