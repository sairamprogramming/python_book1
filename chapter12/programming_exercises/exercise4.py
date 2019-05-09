# Design a function that accepts a list as an argument and returns the largest value in the list.
# The function should use recursion to find the largest item.

import random

def main():
    lst = list(range(1,10))

    random.shuffle(lst)

    maxi = lst[0]

    print(largest(lst, maxi))

def largest(lst, maxi):
    if not lst:
        return maxi
    else:
        if lst[-1] > maxi:
            maxi = lst[-1]
        return largest(lst[:-1], maxi)                

main()    