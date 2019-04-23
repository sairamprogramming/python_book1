# Male and Female percentage.

number_of_males = int(input("Enter the number of males in the class: "))
number_of_females = int(input("Enter the number of females in the class: "))

total_students = number_of_males + number_of_females

males_percent = number_of_males / total_students
males_percent = males_percent * 100

females_percent = number_of_females /  total_students
females_percent = females_percent * 100

print("Percentage of males in the class", format(males_percent, '.2f'))
print("Percentage of females in the class", format(females_percent, '.2f'))