# Kinetic Energy.

# Defining the main function.
def main():
    # Getting user input
    mass = get_mass()   # in kilograms
    velocity = get_velocity()   # in meter / second

    # Calculating the kinetic energy.
    ke = kinetic_energy(mass, velocity)

    # Display the output.
    print("Object has kinetic energy ", format(ke, '.4f'))

# Getting the mass from the user
def get_mass():
    mass = float(input("Enter the mass(in kilograms): "))

    # Input Validation
    while mass < 0:
        print("ERROR!, mass cannot be negative.")
        mass = float(input("Enter the mass(in kilograms): "))
    
    return mass

# Getting velocity from the user.
def get_velocity():
    velocity = float(input("Enter the velocity( in meters / seconds): "))

    # Input Validation.
    while velocity < 0:
        print("ERROR!, velocity cannot be negative.")
        velocity = float(input("Enter the velocity( in meters / seconds): "))
    
    return velocity

# Calculating the kinetic velocity.
def kinetic_energy(mass, velocity):
    return 0.5 * mass * (velocity ** 2)

# Calling the main function.
main()