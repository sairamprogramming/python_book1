# Program to sum digits of a number for a number string.

def main():
    numbers = input("Enter number: ")

    total = 0

    try:
        for digit in numbers:
            total += int(digit)
        
        print(total)
    except:
        print('Invalid Inputs.')

main()