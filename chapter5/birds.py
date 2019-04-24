# This program demonstrates two functions that
# have local variables variable with the same name.

def main():
    # Call the texas funciton.
    texas()
    # Call the california function.
    california()

# Defination of the texas function. It creates 
# a local variable named birds.
def texas():
    birds = 5000
    print('texas has', birds, 'birds')

# Definition of the california function. It also
# creates a local variable named birds.
def california():
    birds = 8000
    print('california has', birds, 'birds.')

# Call the main function.
main()