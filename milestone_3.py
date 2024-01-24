word = "apple"

# The check_guess function will take the guessed letter as an argument
# and check if the letter is in the word
def check_guess(guess):
    # Convert the guess into lower case
    guess = guess.lower()
    # Check if the guess is in the word
    if guess in word:
        # Print a message if the guess is correct
        print(f"Good guess! {guess} is in the word.")
    else:
        # Print a message if the guess is incorrect
        print(f"Sorry, {guess} is not in the word. Try again.")

# The ask_for_input function will ask the user to guess a letter
# and validate it
def ask_for_input():
    # Create a while loop and set the condition to True
    while True:
        # Ask the user to guess a letter and assign this to a variable called guess
        guess = input("Guess a letter: ")
        # Check that the guess is a single alphabetical character
        if len(guess) == 1 and guess.isalpha():
            # If the guess passes the checks, break out of the loop
            break
        else:
            # If the guess does not pass the checks, then print a message
            print("Invalid letter. Please, enter a single alphabetical character.")
    # Call the check_guess function to check if the guess is in the word
    check_guess(guess)

# Call the ask_for_input function to test your code
ask_for_input()