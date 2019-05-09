# Design a function that accepts a string as an argument. Assume that the string will contain
# a single word. The function should use recursion to determine whether the word is a palin-
# drome (a word that reads the same backwards as forward).
# Hint: Use string slicing to refer to and compare the characters on either end of the string.

# The main function.
def main():
    s1 = input('Enter string: ')
    s2 = input('Enter string: ')

    print(is_palindrome(s1,s2))

# The recursive function.
def is_palindrome(s1, s2):
    if not s1 and not s2:
        return True 
    elif s1[-1] != s2[0]:
        return False
    else:
        return is_palindrome(s1[:-1],s2[1:])    

# Calling the main function.
main()        