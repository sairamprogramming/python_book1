def main():
    infile = open('USPopulation.txt', 'r')
    population = []
    for line in infile:
        population.append(int(line))

    diff = []

    for index in range(len(population) - 1):
        diff.append(population[index + 1] - population[index])

    # Finding the average population change. 
    total_diff = sum(diff)

    average_change = total_diff / len(diff)

    
