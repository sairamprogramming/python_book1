# Body Mass Index

# Named constatnt that is multiplier for calulating bmi
BMI_CONSTANT  = 703

# Getting weight and height from the user.
weight = float(input("Enter weight(in pounds): "))
height = float(input("Enter height(in inches): "))

# Calculating bmi from the given user inputs.
bmi = (weight * BMI_CONSTANT) / (height ** 2)

# Finding from given input if the person is under, normal or over weight.
if bmi > 0 and bmi < 18.5:
    print("Under Weight.")
elif bmi >= 18.5 and bmi <= 25.0:
    print("Normal Weight.")
elif  bmi > 25.0:
    print("Over Weight.")
else:
    print("Entered Invalid Inputs.")