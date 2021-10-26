from random import randint
from statistics import mean

from matplotlib import pyplot as plt

from Assignment2_EvolutionaryMastermindSimulator.Logic.Mastermind import Mastermind


def _assignment2_exercise3_line_a():
    def _sorting_method(dictionary: dict):
        return dictionary.get('fitness')

    exercise3_best_percentage = 0.3
    exercise3_goal = "11111111"
    exercise3_sample_size = 100

    def generate_fist_population(goal: str, sample_size: int) -> [dict]:
        # _original_patterns_list: [dict] = []  # (pattern,fitness)
        _patterns_list = []
        _fitnesses_list = []
        for _ in range(0, sample_size):
            _generated_pattern: str = Mastermind.randomBitPattern(size=len(goal))
            # _generated_dict: dict = {
            #    'pattern': _generated_pattern,
            #    'fitness': Mastermind.fitness(goal=goal, curr=_generated_pattern)
            # }
            # _original_patterns_list.append(_generated_dict)

            _patterns_list.append(_generated_pattern)
            _fitnesses_list.append(Mastermind.fitness(goal=goal, curr=_generated_pattern))
        _generated_population = Population(initial_patterns_list=_patterns_list, initial_fitness_list=_fitnesses_list,
                                           initial_goal=goal)
        # _original_patterns_list.sort(reverse=True, key=_sorting_method)
        return _generated_population

    def mutate_population(initial_population: Population, new_pop_size: int, goal: str,
                          best_percentage_mutation: float) -> Population:

        # _initial_pop_size: int = initial_population.get_population_size()

        #_new_best_population: Population = initial_population.extract_best_patterns( best_percentage=best_percentage_mutation)
        _new_best_population: Population = initial_population.extract_max_patterns()

        while _new_best_population.get_population_size() < new_pop_size:
            _chosen_for_mutation: str = _new_best_population.get_random_individual()[0]
            _generated_pattern: str = Mastermind.mutate(input=_chosen_for_mutation, goal=goal)

            # _mutated_individual: dict = {
            #    'pattern': _generated_pattern,
            #    'fitness': Mastermind.fitness(goal=goal, curr=_generated_pattern)
            # }
            _new_best_population.add_individual(pattern=_generated_pattern,
                                                fitness=Mastermind.fitness(goal=goal, curr=_generated_pattern))
        return _new_best_population

    # def population_transpose(pop: [dict]) -> ([str], [int]):
    #    pop_divided: ([str], [int]) = ([], [])
    #    for dict in pop:
    #        pop_divided[0].append(dict.get('pattern'))
    #        pop_divided[1].append(dict.get('fitness'))
    #    return pop_divided

    current_population: Population = generate_fist_population(sample_size=exercise3_sample_size, goal=exercise3_goal)
    mean_fitness_list = []
    counter = 0
    while current_population.mean_fitness() < len(exercise3_goal) and counter <= 1000:
        mutated_pop: Population = mutate_population(new_pop_size=exercise3_sample_size, goal=exercise3_goal,
                                                    initial_population=current_population,
                                                    best_percentage_mutation=exercise3_best_percentage)
        mutated_pop.extract_max_patterns()
        current_population = mutated_pop
        mean_fitness_list.append(current_population.mean_fitness())
        counter += 1
        print("counter", counter, "pop", current_population)

    plt.plot(mean_fitness_list)
    plt.tight_layout()
    plt.show()

    # _first_population = generate_fist_population(goal=exercise3_goal)
    # mutated_population: [dict] = mutate_population(initial_population=_first_population, new_pop_size=exercise3_sample_size, goal=exercise3_goal)
    # print("Assignment2::Exercise3::population:",mutated_population)
    # print("Assignment2::Exercise3::length of populaton:",len(mutated_population))
    # print("Assignment2::Exercise3::population transposed:patterns:",population_transpose(mutated_population)[0])
    # print("Assignment2::Exercise3::population transposed:fitness_values:",population_transpose(mutated_population)[1])


class Population:
    def __str__(self) -> str:
        string_output: str = "mean_Fitness=" + str(self.mean_fitness()) + ";\tpop_size=" + str(
            self.get_population_size()) + \
                             ";\tpatterns:" + str(self._patterns_list) + ";fitnesses:" + str(self._fitness_list)
        return string_output

    _patterns_list: [str] = []
    _fitness_list: [int] = []
    _goal: str

    def __init__(self, initial_goal: str, initial_patterns_list: [str] = None, initial_fitness_list: [int] = None, ):
        self._patterns_list = initial_patterns_list
        self._fitness_list = initial_fitness_list
        self._goal = initial_goal

    def add_individual(self, pattern: str, fitness: int = None) -> None:
        if fitness is None:
            fitness = Mastermind.fitness(curr=pattern, goal=self._goal)
        self._patterns_list.append(pattern)
        self._fitness_list.append(fitness)

    def get_population_size(self):
        return len(self._fitness_list)

    def get_pattern_values(self) -> [str]:
        return self._patterns_list

    def get_fitness_values(self) -> [int]:
        return self._fitness_list

    def get_random_individual(self) -> (str, int):
        _random_index = randint(0, self.get_population_size() - 1)

        result = (self._patterns_list[_random_index], self._fitness_list[_random_index])
        return result

    def mean_fitness(self) -> float:
        return mean(self._fitness_list)

    def extract_best_patterns(self, best_percentage: float):
        _original_fitnesses = self._fitness_list.copy()
        _original_patterns = self._patterns_list.copy()

        _zipped = list(zip(_original_patterns, _original_fitnesses, ))
        _sorted_zip = sorted(_zipped, key=lambda x: x[1], reverse=True)

        _best_fitnesses = []
        _best_patterns = []
        for index in range(int(best_percentage * len(_sorted_zip))):
            _best_patterns.append(_sorted_zip[index][0])
            _best_fitnesses.append(_sorted_zip[index][1])

        best_population = Population(initial_goal=self._goal,
                                     initial_fitness_list=_best_fitnesses, initial_patterns_list=_best_patterns
                                     )
        return best_population

    def extract_max_patterns(self):
        _original_fitnesses = self._fitness_list.copy()
        _original_patterns = self._patterns_list.copy()

        _zipped = list(zip(_original_patterns, _original_fitnesses, ))
        _sorted_zip = sorted(_zipped, key=lambda x: x[1], reverse=True)
        max_fitness = _sorted_zip[0][1]
        _new_individuals_pattern: [str] = []
        _new_individuals_fitness: [int] = []
        for item in _sorted_zip:
            if item[1] < max_fitness: break
            _new_individuals_pattern.append(item[0])
            _new_individuals_fitness.append(item[1])

        return Population(initial_goal=self._goal,
                          initial_patterns_list=_new_individuals_pattern, initial_fitness_list=_new_individuals_fitness,
                          )


if __name__ == '__main__':
    _assignment2_exercise3_line_a()
