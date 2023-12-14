population = list(map(int, input().split(", ")))
minimum_wealth = int(input())
max_number = - 100000000
all_wealth = 0

for number in population:
    all_wealth += int(number)
number_people = len(population)
average_wealth_per_person = all_wealth / number_people

if average_wealth_per_person >= minimum_wealth:

    for person in range(len(population)):
        if population[person] < minimum_wealth:
            difference_that_we_should_add = minimum_wealth - population[person]
            for number in range(len(population)):
                if population[number] > max_number:
                    max_number = population[number]
            max_number_index = population.index(max_number)
            max_number = -100000000
            population[person] += difference_that_we_should_add
            population[max_number_index] -= difference_that_we_should_add
    print(population)
else:
    print("No equal distribution possible")