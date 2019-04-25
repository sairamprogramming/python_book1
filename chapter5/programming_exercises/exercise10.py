# Feet to Inches

# Cosntant used since, 1 foot = 12 inches
FOOT_INCHES_CONVERTER = 12.0

# Defining the main funciton.
def main():
    # Getting the input from the user.
    feet_input = get_feet()

    # Calculating the amount of inches from the feet given by the user.
    inches = feet_to_inches(feet_input)

    # Display the output.
    print(feet_input, "converted to feet is", format(inches, ',.2f'))

# This function gets and returs the number of feet to convert form the user.
def get_feet():
    feet = float(input("Enter the amount in feet: "))

    # Input Validiation.
    while feet < 0:
        print("ERROR!, feet cannot be negative.")
        feet = float(input("Enter the amount in feet: "))
    
    return feet

# This fucntion converts the feet given by the user to inches and returns the value.
def feet_to_inches(feet):
    inches = feet * FOOT_INCHES_CONVERTER
    return inches

# Calling the main function.
main()