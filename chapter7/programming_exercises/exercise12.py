# File Line Viewer

# Write a program that asks the user for the name of a file. The program should read all of
# the file’s data into a list and display the number of lines of data that the file contains, and
# then ask the user to enter the number of the line that they want to view. The program should
# display the specified line.
# 
# The program should handle the following exceptions by displaying an error message:
# • IOError exceptions that are raised when the specified filename cannot be found or
#   opened.
# • ValueError exceptions that are raised when a non-integer value is given as a line number.
# • IndexError exceptions that are raised when the line number is outside the range of the
#   data list

def main():
    # Getting filename from the user.
    filename = input("Enter the file name: ")

    # Handling IOError.
    try:
        infile = open(filename, 'r')
    except IOError:
        print("Error: File not found!")
        return

    # Writing all lines into a list.
    lst = []

    for line in infile:
        lst.append(line.strip())

    # Handling ValueError.
    try:
        line_number = int(input("Enter the number line: "))                            
    except ValueError:
        print("Error: Format of given input is not integer type.")        
        return

    # Handling IndexError.
    try:
        print(lst[line_number - 1])
    except IndexError:
        print('Error: Given index is out of range.')        
        return