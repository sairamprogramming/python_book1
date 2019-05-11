def main():
    # Creating the population list.
    infile = open('USPopulation.txt', 'r')
    population = []
    for line in infile:
        population.append(int(line))
    infile.close()

    # Making a list of population differences.
    diff = []

    for index in range(len(population) - 1):
        diff.append(population[index + 1] - population[index])

    # Finding the average population change. 
    total_diff = sum(diff)

    average_change = total_diff / len(diff)

    # Finding the max year and min year.
    max_index = 0
    min_index = 0

    for index in range(len(diff)):
        if diff[index] > diff[max_index]:
            max_index = index
        if diff[index] < diff[min_index]:
            min_index = index

    # Printing the output.
    print("The average annual change is ", average_change)            
    print("The year with the greatest increase in population", max_index + 1950 + 1)            
    print("The year with teh smallest increase in population", min_index + 1 + 1950)

# Calling the main function.
main()    

    
