# Planting Grapevines

# Formula implemented: V = (R - 2E) / S

row_length = float(input("Enter length( in feet ): "))
end_post_space = float(input("Enter space used by the end post: "))
space_between_vines = float(input("Enter the space between vines: "))

number_of_vines = (row_length - 2 * end_post_space) / space_between_vines

print("The number of vines that can be planted is", int(number_of_vines))