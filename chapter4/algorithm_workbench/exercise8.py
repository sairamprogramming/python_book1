# Input Validation

number = int(input("Enter a positive non zero number: "))

while number <= 0:
    print("ERROR! You have entered a invalid number.")
    number = int(input("Enter a positive non zero number: "))

print("Number you have entered is", number)
