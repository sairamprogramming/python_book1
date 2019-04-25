# Rock, Paper, Scissors Game.
import random

# Defining the main function.
def main():
    # Getting the computers choice.
    computer_hand = get_computer_hand()

    # Getting the players choice.
    player_hand = get_player_hand()

    # Getting the winner of the game.
    winner = game(player_hand, computer_hand)

    # Display the output
    print('The computer choose', computer_hand)

    if winner == 'player' or winner == 'computer':
        print(winner, 'wins!')
    else:
        print('The game is a draw.')
        

# This function get the computer's choice of the 3 options.
def get_computer_hand():
    hand = random.randint(1, 3)

    if hand == 1:
        return "rock"
    elif hand == 2:
        return "paper"
    else:
        return "scissors"

# Getting the player choice from the user.
def get_player_hand():
    hand = input("Enter your choice(rock, paper or scissors): ")

    # Input validation.
    while hand != 'rock' and hand != 'paper' and hand != 'scissors':
        print("Invalid Inputs, Try again.")
        hand = input("Enter your choice(rock, paper or scissors): ")
    
    return hand

# Function returns True if player wins
def player_win_condition(player_hand, computer_hand):

    if player_hand == 'rock' and computer_hand == 'scissors':
        return True
    
    if player_hand == 'paper' and computer_hand == 'rock':
        return True
    
    if player_hand == 'scissors' and computer_hand == 'paper':
        return True
    
    return False

# Function returns True if game is draw.    
def player_draw_condtion(player_hand, computer_hand):
    return player_hand == computer_hand

# This the main body of the game logic.
# We do not check the player loss (or computer win condtion), since it is the only choice only left if 
# eleminate the other 2 choices of the game result.
def game(player_hand, computer_hand):

    if player_win_condition(player_hand, computer_hand):
        return 'player'
    elif player_draw_condtion(player_hand, computer_hand):
        return 'draw'
    else:
        return 'computer'

# Calling the main function.
main()