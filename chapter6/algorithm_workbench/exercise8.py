# This program modify 'Julie Milan' record in the students.txt file

import os       # This module is needed to remove and rename a file.

def main():
    # bool to see if record is in file
    found = False

    # Opening the students.txt file in read mode
    students_file = open('students.txt', 'r')
    # Opening the temp.txt in write mode
    temp_file = open('temp.txt', 'w')

    # Getting the item to modify
    item_modify = 'Julie Milan'
    new_score = 100

    # Reading the inital name from the file students.txt
    name = students_file.readline()

    # Deleting the record
    while name != '':
        name = name.rstrip('\n')
        # reading the students score from the file students.txt
        score = students_file.readline()
        
        # Writing to temp all records except 'Julie Milan'
        if name != item_modify:
            temp_file.write(name + '\n')
            temp_file.write(score)
        else:
            temp_file.write(name + '\n')
            temp_file.write(str(new_score) + '\n')
            found = True

        name = students_file.readline()
    
    # Closing the two files
    students_file.close()
    temp_file.close()

    # Printing the result of operation.
    if found:
        print('Item is modified in the file students.txt')
    else:
        print('Item not in file students.txt')
    
    # Deleating the file studets.txt
    os.remove('students.txt')
    # Renaming temp.txt to students.txt
    os.rename('temp.txt', 'students.txt')

# Calling the main function.
main()
