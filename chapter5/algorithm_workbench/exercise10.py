def is_valid(string, number):
    if len(string) > number:
        return False
    return True

print(is_valid('abcd', 5))
print(is_valid('abcdef', 5))
