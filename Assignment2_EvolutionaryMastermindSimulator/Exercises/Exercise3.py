from matplotlib import pyplot as plt

from Assignment2_EvolutionaryMastermindSimulator.Logic.Population import Population, mutate_population

exercise3_max_generations = 100


def _assignment2_exercise3_line_a():

    exercise3_best_percentage = 0.3
    exercise3_goal = "11111111"
    exercise3_sample_size = 100

    current_population: Population = Population.generate_fist_population(sample_size=exercise3_sample_size,
                                                                         goal=exercise3_goal)
    mean_fitness_list = []
    counter = 0
    while current_population.mean_fitness() < len(exercise3_goal) and counter <= exercise3_max_generations:
        mutated_pop: Population = mutate_population(new_pop_size=exercise3_sample_size, goal=exercise3_goal,
                                                    initial_population=current_population,
                                                    best_percentage_mutation=exercise3_best_percentage,
                                                    )

        current_population = mutated_pop
        mean_fitness_list.append(current_population.mean_fitness())
        counter += 1
        print("counter", counter, "pop", current_population)

    plt.plot(mean_fitness_list)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    _assignment2_exercise3_line_a()
