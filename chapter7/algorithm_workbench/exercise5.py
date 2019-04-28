# Program to pass a list as an argument to
# a function and the function to find the 
# total of the list.
import random

def main():
    number_list = []

    for i in range(10):
        number_list.append(random.randint(1, 10))
    
    total = get_total(number_list)

    print(number_list)
    print(total)

# Function that finds the total of the list 
# passed on to it.
def get_total(value_list):
    total = 0.0

    for number in value_list:
        total += number
    
    return total

main()