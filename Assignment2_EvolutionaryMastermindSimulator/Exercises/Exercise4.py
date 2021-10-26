from matplotlib import pyplot as plt

from Assignment2_EvolutionaryMastermindSimulator.Logic.Population import Population, mutate_population

exercise3_max_generations = 100


def _assignment2_exercise4_line_a():

    exercise4_best_percentage = 0.3
    exercise4_goal = "11111111"
    exercise4_sample_size = 100

    current_population: Population = Population.generate_fist_population(sample_size=exercise4_sample_size,
                                                                         goal=exercise4_goal)
    mean_fitness_list = []
    counter = 0
    while current_population.get_mean_fitness() < len(exercise4_goal) and counter <= exercise3_max_generations:
        mutated_pop: Population = mutate_population(new_pop_size=exercise4_sample_size, goal=exercise4_goal,
                                                    initial_population=current_population,
                                                    best_percentage_mutation=exercise4_best_percentage)
        current_population = mutated_pop
        mean_fitness_list.append(current_population.get_mean_fitness())
        counter += 1
        print("counter", counter, "pop", current_population)

    plt.plot(mean_fitness_list)
    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    _assignment2_exercise4_line_a()
