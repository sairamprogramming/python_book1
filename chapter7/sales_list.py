# The NUM_DAYS constant holds the number of 
# days that we will gather sales data for.
NUM_DAYS = 5

def main():
    # Create a list to hold sales
    # for each day.
    sales = [0] * NUM_DAYS

    # Create a varialbe to hold an index.
    index = 0

    print('Enter the sales for each day')

    # Get the sales for each day.
    while index < NUM_DAYS:
        print('Day #', index + 1, ': ', sep = '', end = '')
        sales[index] = float(input())
        index += 1
    
    # Display the values entered here:
    for value in sales:
        print(value)

# Call the main function.
main()