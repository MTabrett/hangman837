import random


class Hangman:   
    '''
    A simple Hangman game class.

    Args:
        available_word_list (list): List of available words for the game.
        number_lives_start (int, optional): Number of lives for the player. Defaults to 5.
    '''
    def __init__(self, available_word_list, number_lives_start:int=5):
        '''
        Initializes the Hangman game.

        Args:
            available_word_list (list): List of available words for the game.
            number_lives_start (int, optional): Number of lives for the player. Defaults to 5.
        '''
        self.random_selected_word = random.choice(available_word_list)
        self.word_guessed = ["_" for _ in self.random_selected_word]
        print(*self.word_guessed)
        self.number_letters = len(self.random_selected_word)
        print(f"The mystery word has {self.number_letters} characters")
        self.number_lives = number_lives_start
        self.word_list = available_word_list
        self.list_of_guesses = []
    
    def check_guess_correct(self, players_guess): 
        '''
        Checks if the player's guess is correct and updates the game state.

        Args:
            players_guess (str): The guessed letter.

        Returns:
            None
        '''           
        if players_guess in self.random_selected_word:
            print(f"Good guess! {players_guess} is in the word.")      
            for letter in range(len(self.random_selected_word)):
                if self.random_selected_word[letter] == players_guess:
                    self.word_guessed[letter] = players_guess
                    self.number_letters -= 1
        else:
            self.number_lives -= 1
            print(f"Sorry, {players_guess} is not in the word.")
            print(f"You have {self.number_lives} lives left.")   
                       
    def ask_player_for_input(self):
        '''
        Asks the player for a letter guess and validates the guess and then updates game state.

        Returns:
            None
        '''
        while True:
            players_guess = input("Guess a letter: ").lower()
            # Create an if statement that runs if the guess is NOT a single alphabetical character         
            if len(players_guess) != 1 or not players_guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")            
            elif players_guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess_correct(players_guess)
                self.list_of_guesses.append(players_guess)
                print(players_guess)
                print(*self.word_guessed)
                break             

def play_game(word_list):
    '''
    Plays the Hangman game.

    Args:
        word_list (list): List of available words for the game.

    Returns:
        None
    '''
    number_lives = 5
    game = Hangman(word_list, number_lives)
    while True:
        if game.number_lives == 0:
            print("You lost!")
            break
        elif game.number_letters > 0:
            game.ask_player_for_input()
        else:
            print("Congratulations. You won the game!")
            break

if __name__ == "__main__":
    available_word_list = ["grape", "grapefruit", "gooseberry", "lychee", "blueberry"] 
    play_game(available_word_list)
 