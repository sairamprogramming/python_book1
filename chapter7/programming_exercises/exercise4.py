# Number Analysis Program.

# Program gets 20 numbers from the user and finds:
# Lowest number in the list.
# Highest number in the list.
# Total of numbers in the list.
# Average of numbers in the list.

NUMBER_OF_ELEMENTS = 20

def main():
    # Getting 20 numbers from the user.
    number_list = []

    for unused_variable in range(NUMBER_OF_ELEMENTS):
        # Here we make sure to get the input in the correct format.
        # We also make sure input will not give exceptions down the line.
        incorrect_input = True

        while incorrect_input:
            try:
                input_number = float(input("Enter a number: "))
                incorrect_input = False
            except ValueError:
                print("Invalid Input, try again!")

        number_list.append(input_number)
    
    # Initalizing variables to find the required quantites..
    lowest_number = number_list[0]
    highest_numer = number_list[0]
    total = 0.0

    for number in number_list:
        # Finding the lowest number.
        if number < lowest_number:
            lowest_number = number

        # Finding the highest number.
        if number > highest_numer:
            highest_numer = number
        
        # Calculating the total.
        total += number

    # Calculating the average.
    average = total / len(number_list)

    # Displaying the output.
    print('List:', number_list)
    print('Lowest Number:', lowest_number)
    print('Highest Number:', highest_numer)
    print('Total:', total)
    print('Average:', average)

# Call the main function.
main()    