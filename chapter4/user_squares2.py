# This program uses a loop to display a
# table of number and their and squares.

# Get the starting value and ending limit.
print('This program diplays a list of numbers.')
print('(starting at 1) and their squares.')
start = int(input('Enter the starting number: '))
end = int(input('How high should I go? '))

# Print the table headings.
print()
print('Number\tSquare')
print('--------------')

# Print the numbers and their squares.
for number in range(start, end + 1):
    square = number ** 2
    print(number, '\t', square)