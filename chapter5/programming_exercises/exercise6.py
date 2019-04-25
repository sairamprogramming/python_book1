# Calories from Fat and Carbohydrates.

# Constant converts fat(in grams) to calories.
FAT_CALORIES_CONSTANT = 9
# Constant converts carbohydrates(in grams) to calories.
CARBOHYDRATES_CALORIES_COSNTANT = 4

# Defines the main function.
def main():
    # Getting input from the user.
    fat_consumed = get_fat_consumed()
    carbohydrates_consumed = get_carbohydrates_consumed()

    # Calculating the calories from fat and carbohydates.
    fat_calories = calories_from_fat(fat_consumed)
    carbohydrates_calories = calories_from_carbohydrates(carbohydrates_consumed)

    # Display the output.
    print('The calories from fat is ', format(fat_calories, '.2f'))
    print('The calories from carboydrates is', format(carbohydrates_calories, '.2f'))

# Getting fat consumed(in grams) from the user.
def get_fat_consumed():
    fat_consumed = float(input("Enter the amount of fat consumed(in grams): "))

    while fat_consumed < 0:
        print("'fat_consumed' cannot be negative !")
        fat_consumed = float(input("Enter the amount of fat consumed(in grams): "))
    
    return fat_consumed

# Getting the carbohydrates consumned(in grams) from the user.
def get_carbohydrates_consumed():
    carbohydrates_consumed = float(input("Enter the amount of carbohydrates consumed(in grams): "))

    while carbohydrates_consumed < 0:
        print("'carbohydrates_consumed' cannot be negative!")
        carbohydrates_consumed = float(input("Enter the amount of carbohydrates consumed(in grams): "))
    
    return carbohydrates_consumed

# Calculating calories from fat consumed.
def calories_from_fat(fat_consumed):
    fat_calories = fat_consumed * FAT_CALORIES_CONSTANT
    return fat_calories

# Calculating calories from carbohydrates consumed.
def calories_from_carbohydrates(carbohydrates_consumed):
    carbohydrates_calories = carbohydrates_consumed * CARBOHYDRATES_CALORIES_COSNTANT
    return carbohydrates_calories

# Calling the main funciton.
main()