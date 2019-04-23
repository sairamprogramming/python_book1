# Input Validation

number = int(input("Enter a number between 1 and 100 (inclusive): "))

while number < 1 or number > 100:
    print("ERROR! you have entered a number outside the valid range.")
    number = int(input("Enter a number between 1 and 100 (inclusive): "))

print("Number you have entered is", number)
