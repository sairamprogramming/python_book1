# Exception Handling.

def main():
    try:
        # Open the file.
        infile = open('numbers.txt', 'r')

        # Initalize the total accumulator.
        total = 0
        # Accumulator to keep track of the number of items in the file.
        count = 0

        # Read all the numbers in the file.
        for number in infile:
            # Sum all the numbers.
            number = int(number)
            total += number
            count += 1
        
        # Calculate average.
        average = total / count

        # Close the file and print the average.
        infile.close()
        print('Average of numbers:', average)
    except IOError:
        print("File not found!")
    except ValueError:
        print("Invalid Input!")
    except:
        print('Error!')

# Call the main function.
main()