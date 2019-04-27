# This program displays the records that are 
# in the employee.txt file.

def main():
    # Open the employees.txt file.
    emp_file = open('employee.txt', 'r')

    # Read the first line from the file, which is
    # the name field of the first record.
    name = emp_file.readline()

    # If a field was read continue processing.
    while name != '':
        # Read the ID number field.
        id_num = emp_file.readline()

        # Read the department field.
        dept = emp_file.readline()

        # Strip the newlines from the fields.
        name = name.rstrip('\n')
        id_num = id_num.rstrip('\n')
        dept = dept.rstrip('\n')

        # Display the records.
        print('Names:', name)
        print('ID:', id_num)
        print('Dept:', dept)
        print()

        # Read the name field of the next record.
        name = emp_file.readline()
    
    # Close the file.
    emp_file.close()

# Call the main function.
main()