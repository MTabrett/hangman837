# Project Title - Hangman: A Classic Word guessing Game in Python
![Alt text](hangman.png)

Hangman is a classic word guessing game where the computer randomly choices a word and the player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it.

## Table of Contents
1. Introduction (#project title)
2. Project Description (#project description)
3. Installation Instructions (#installation instructions)
4. Usage Instructions (#Usage instructions)
5. License Information

## Project Description
In the classic children's game of Hangman, a player's objective is to identify a secret word of which only the number of letters is originally revealed. In each round, the player guesses a letter of the alphabet: if it is present in the secret word, all instances are revealed; otherwise one of the hangman's body parts is drawn in on a gibbet. The game ends in a win if the word is entirely revealed by correct guesses, and ends in a loss if the hangman's body is completely revealed instead. To assist the player, a visible record of all guessed letters is typically maintained.

    - Creates a list of words that the computer Randomly selects a word from
    - Player inputs guessed letter
    - Computer checks that the entered guess is only 1 letter and is alphabetical
    - Prints a response dependent on valid or invalid input
    - If input valid Displays the guessed letters and the word progress
     - Shows the hangman stages as you make wrong guesses
     - Checks the user input a valid entry
     - Tells you if you win or lose the game

## Installation instructions
    To install the game, you need to have Python 3 installed on your system. You can download it from [here](https://www.python.org/downloads/).

Then, you can clone this repository or download the zip file. To clone the repository, run the following command:

''' bash
git clone https://github.com/MTabrett/hangman_game_project.git
import random
run milestone_2.py to start the game

## Usage instructions
    To play the game, navigate to the project directory and run the milestone_2.py file:


## License information
MIT license