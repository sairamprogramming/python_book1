# Valid Number Information.

# Build list of valid numbers (0 to 100 inclusive) 
# and find the total and average of this valid 
# numbers list.

def main():
    numbers = [74, 19, 105, 20, -2, 67, 77, 124, -45, 38]

    # Creating the valid_numbers list.
    valid_numbers = []

    for number in numbers:
        if number >= 0 and number <= 100:
            valid_numbers.append(number)
    
    # Finding the total of valid_numbers list.
    total = 0.0

    for number in valid_numbers:
        total += number
    
    # Calculating the average.
    average = total / len(valid_numbers)

    # Display the output.
    print("Total:", total)
    print("Average:", format(average, '.3f'))

# Call the main function.
main()