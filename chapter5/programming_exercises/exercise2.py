# String Repeater

# Defining the main function.
def main():
    result = repeat('Hi', 3)
    print(result)

# Defining the repeat function (not using the 'hi' * 3 function built in python)
def repeat(string, times_to_repeat):
    output_string = ''

    for i in range(times_to_repeat):
        output_string += string
    
    return output_string

# Calling the main funciton
main()