# Book Club Points

# Getting the number of books purchased from the user.
number_of_books = int(input("Enter the number of books purchased: "))

# Finding the points to be awarded based on the number of purchased books.
if number_of_books >= 0 and number_of_books < 2:
    points = 0
elif number_of_books >= 2 and number_of_books < 4:
    points = 5
elif number_of_books >= 4 and number_of_books < 6:
    points = 15
elif number_of_books >= 6 and number_of_books < 8:
    points = 30
elif number_of_books >= 8:
    points = 60

# Displaying the number of points awarded.
print('The number points you have been awarded:', points)