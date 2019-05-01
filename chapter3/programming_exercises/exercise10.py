# Money Counting Game.

# In this program you enter an amount in denominations of dollars
# and try to reach exact one dollar to win the game.

# Getting input from the user.
pinnes = float(input("Enter the amount of pennies: "))
nickels = float(input("Enter the amount of nickels: "))
dimes = float(input("Enter the amount of dimes: "))
quarters = float(input("Enter the amount of dollars: "))

# Converting all the denominations to dollars.
dollar = 0

dollar += pinnes * 0.01
dollar += nickels * 0.05
dollar += dimes * 0.1
dollar += quarters * 0.25

# Check to see if you won the game.
if dollar == 1:
    print("You won the game.")
elif dollar > 1:
    print("You have entered an amount greater than $1.")
else:
    print("You have entered an amount less than $1.")