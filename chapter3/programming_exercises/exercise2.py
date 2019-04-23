# Areas of rectangles.

# Getting the input of length and width of the two rectangles.
length1 = int(input("Enter the length of the first rectangle: "))
width1 = int(input("Enter the width of the first rectangle: "))

length2 = int(input("Enter the length of the second rectangle: "))
width2 = int(input("Enter the length of the second rectangle: "))

# Finding the area of the two rectangles.
area1 = length1 * width1
area2 = length2 * width2

# Display the area
print("Area of the first rectanggle is", area1)
print("Area of the second rectangle is", area2)

# Checking which rectangle is bigger.
if area1 > area2:
    print("First rectangle has greater area than the second rectange.")
elif area2 > area1:
    print("Second rectangle has greater area than the first rectange.")
else:
    print("The two rectangeles have the same area.")