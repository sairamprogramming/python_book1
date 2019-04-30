# Charge Account Validation.

# Program to see if an account number, given by
# the user is valid.

def main():
    # Opening file in read mode.
    infile = open('charge_accounts.txt', 'r')

    # Initalzing list to hold account numbers from file.
    valid_account_numbers = []

    # Getting the initial account number to validate,
    # while loop.
    account_number = infile.readline()

    # Getting all accunt numbers into a list.
    while account_number != '':
        account_number = int(account_number)
        valid_account_numbers.append(account_number)
        account_number = infile.readline()
    
    # Closing the file.
    infile.close()

    # Exception handling to get input in correct format.
    try:
        # Getting the account number form the user.
        user_account = int(input("Enter account number: "))

        # Check and display in account number entered by
        # the user is valid.
        if user_account in valid_account_numbers:
            print("Entered account number is valid.")
        else:
            print("Entered account number is invalid.")
    except ValueError:
        print("Invalid account number format!")

# Calling the main function.
main()