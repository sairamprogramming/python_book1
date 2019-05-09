# Design a function that accepts a list of numbers as an argument. The function should recur-
# sively calculate the sum of all the numbers in the list and return that value.

import random

# The main function definition.
def main():
    lst = list(range(1,10))

    random.shuffle(lst)

    print(total(lst,len(lst)-1))

# The recurisive case.
def total(lst, index):
    # Base Case.
    if index == -1:
        return 0
    # Recursive Case.
    else:
        return lst[index] + total(lst, index - 1)

# Calling the main function.
main()        