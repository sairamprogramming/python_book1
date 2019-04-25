# Random Number guessing Game
import random

# Initalizing the intital random guess number
GUESS_NUMBER = random.randint(1, 100)


# Defining the main function
def main():
    print("\n\nTHIS IS THE NUMBER GUESSING GAME")
    
    # Initalizing to count the number of guesses. ('1' since we do not count the last correct input from the user.)
    count_guesses = 1

    # Getting the inital guess
    number_input = get_number()

    # Getting number inputs from the user, till we get the guessed number.
    while number_input != GUESS_NUMBER:
        if number_input > GUESS_NUMBER:
            print("Too high, try again.")
        elif number_input < GUESS_NUMBER:
            print("Too low, try again.")

        count_guesses += 1        
        number_input = get_number()
    
    # Display the output.
    print("You guessed the number!!!")
    print("You took", count_guesses, "to guess the number!")

# This function gets the input from the user.
def get_number():
    number = int(input('Enter the number: '))

    while number < 1 or number > 100:
        print("Invalid Input, Enter input again.")
        number = int(input('Enter the number: '))
    
    return number

# Calling the main function.
main()