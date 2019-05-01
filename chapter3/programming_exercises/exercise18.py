# Resturant Selector.

# Getting input from the user.
print("Enter 'yes' for yes and anything else is no.")
choice_vegetarian = input("Is anyone in your party a vegetarian? ")
choice_vegan = input("Is anyone in your party a vegan? ")
choice_gulten = input("Is anyone in your party a gulten-free? ")

# Assiging boolean to variables for ease of using in the program.
vegetarian = choice_vegetarian == 'yes'
vegan = choice_vegan == 'yes'
gulten_free = choice_gulten == 'yes'

# Displaying the choice of resturant depending on the input.
if vegetarian and vegan and gulten_free:
    print("Corner Cafe")
    print("The Chef's Kitchen")
elif vegetarian and vegan:
    print("Corner Cafe")
    print("The Chef's Kitchen")
elif vegetarian and gulten_free:
    print("Main Street Pizza Company")
    print("Corner Cafe")
    print("The Chef's Kitchen")
elif vegetarian:
    print("Mama's Fine Kitchen")
elif not vegetarian and not vegan and not gulten_free:
    print("Joe's Gorment Resturant")
else:
    print("We have no choice of restruant that meet your requirements.")
