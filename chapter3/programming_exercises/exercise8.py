# Hot Dog CookOut Calculator

# Named constants representing the number of hot dogs and number of hot dog buns per bag.
NUMBER_HOT_DOG_PER_BAG = 10
NUMBER_HOT_DOG_BUN_PER_BAG = 8

# Getting input from the user on the number of people attending the cookout and how many
# hot dogs each person consumes.
total_people = int(input("Total Number of people attending the cookout: "))
hot_dog_per_person = int(input("NUmber of hot dogs each person consumes: "))

# Calculating the total number of hot dogs required for the cookout.
total_hot_dogs = total_people * hot_dog_per_person

# Calculating the number of bags of hot dogs and number of bags of hot dog bus required
# for the cookout.
if total_hot_dogs % NUMBER_HOT_DOG_BUN_PER_BAG != 0:
    hot_dog_bags = (total_hot_dogs // NUMBER_HOT_DOG_PER_BAG) + 1
else:
    hot_dog_bags = total_hot_dogs // NUMBER_HOT_DOG_PER_BAG
    
if total_hot_dogs % NUMBER_HOT_DOG_BUN_PER_BAG != 0:
    bun_bags = (total_hot_dogs // NUMBER_HOT_DOG_BUN_PER_BAG) + 1
else:
    bun_bags = total_hot_dogs // NUMBER_HOT_DOG_BUN_PER_BAG

# Calculating the number of left over hot dogs and hot dog buns
left_over_hot_dogs = (hot_dog_bags * NUMBER_HOT_DOG_PER_BAG) - total_hot_dogs 
left_over_buns = (bun_bags * NUMBER_HOT_DOG_BUN_PER_BAG) - total_hot_dogs

# Diplaying the required output.
print("The minimum number of hot dog bags required for cookout is", hot_dog_bags)
print("The minimum number of hot dog bun bags required for cookout is", bun_bags)
print("Left over hot dogs:", left_over_hot_dogs)
print("Left over hot dog buns:", left_over_buns)