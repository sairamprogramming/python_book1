# This program deletes 'John Perz' record from the students.txt file

import os       # This module is needed to remove and rename a file.

def main():
    # bool to see if record is in file
    found = False

    # Opening the students.txt file in read mode
    students_file = open('students.txt', 'r')
    # Opening the temp.txt in write mode
    temp_file = open('temp.txt', 'w')

    # Getting the item to delete
    item_delete = 'John Perz'

    # Reading the inital name from the file students.txt
    name = students_file.readline()

    # Deleting the record
    while name != '':
        name = name.rstrip('\n')
        # reading the students score from the file students.txt
        score = students_file.readline()
        
        # Writing to temp all records except 'John Perz'
        if name != item_delete:
            temp_file.write(name + '\n')
            temp_file.write(score)
        else:
            found = True

        name = students_file.readline()
    
    # Closing the two files
    students_file.close()
    temp_file.close()

    # Printing the result of operation.
    if found:
        print('Item is deleted from the file students.txt')
    else:
        print('Item not in file students.txt')
    
    # Deleating the file studets.txt
    os.remove('students.txt')
    # Renaming temp.txt to students.txt
    os.rename('temp.txt', 'students.txt')

# Calling the main function.
main()
