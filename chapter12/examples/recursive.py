# This program has a recurisve function.

def main():
    # By passing the argument 5 to the message
    # function we are telling it to display the
    # message 5 times.
    message(5)

def message(time):
    if time > 0:
        print("This is a recursive function.")
        message(time - 1)    

# Call the main function.
main()        