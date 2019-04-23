# Mass and Weights
# weight = mass + 9.8

# This named constant is acceleration due to gravity of earth on an object.
GRAVITY_ACCELERATION = 9.8

# Get the value of mass to conver from the user in Kg.
mass = float(input('Emter mass(in kilograms): '))

# Calculate the weight in Newtons.
weight = mass * GRAVITY_ACCELERATION

# Display the weight
print("Weight of the object is", format(weight, '.3f'), "Newtons.")

# Main part of exercise 5
# Check if the object is too heavy( > 500 Newtons) or too light( < 100 Newtons)
if weight > 500:
    print("object is too heavy.")
elif weight < 100:
    print("object is too light.")