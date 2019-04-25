# main function
def main():
    string_input = input("Enter a string: ")
    shout(string_input)

# defining shout.
def shout(string):
    string_uppercase = string.upper()
    output_string = string_uppercase + "!"
    print(output_string)

# Calling main function.
main()