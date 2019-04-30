# Alphabetic Telephone Number Translator.

# Tuple Mapping the alphabets to the respective numbers.
TELEPHONE_MAP = (
                    (('A','B','C'), 2),
                    (('D','E','F'), 3),
                    (('G','H','I'), 4),
                    (('J','K','L'), 5),
                    (('M','N','O'), 6),
                    (('P','Q','R','S'), 7),
                    (('T','U','V'), 8),
                    (('W','X','Y','Z'), 9)
                    )

def main():
    # Get the alphanumeric phone number from the user.
    ph_number = input('Get the phone number: ')
    # Split it to list using '-' as argument.
    ph_number = ph_number.split('-')

    # This list holds the converted phone number.
    converted_ph_number = []    


    for item in ph_number:
        # This variable is hold the converted section of the given number.
        temp_list = ''

        # Checking every charater in the phone number.
        # Converting character to appropriate number.
        for ch in item:
            #  If character is digit, do nothing and add it to temp_list as is.
            if ch.isdigit():
                temp_list += ch
            # If character is alphabet, convert it to number and add it to temp_list.
            elif ch.isalpha():
                ch = ch.upper()

                for code in TELEPHONE_MAP:
                    if ch in code[0]:
                        temp_list += str(code[1])
                        break

        # Append the section.
        converted_ph_number.append(temp_list)
    
    # Join all the strings in the list using '-' as argument.
    converted_ph_number = '-'.join(converted_ph_number)

    # Display the output.
    print(converted_ph_number)

# Call the main function.
main()
        