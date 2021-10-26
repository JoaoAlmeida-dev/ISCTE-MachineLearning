from random import randint
from statistics import mean

from Assignment2_EvolutionaryMastermindSimulator.Logic.Mastermind import Mastermind


class Population:
    def __str__(self) -> str:
        string_output: str = "mean_Fitness=" + str(self.get_mean_fitness()) + ";\tpop_size=" + str(
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

    def get_mean_fitness(self) -> float:
        return mean(self._fitness_list)

    def sort(self):
        _original_fitnesses = self._fitness_list.copy()
        _original_patterns = self._patterns_list.copy()

        _zipped = list(zip(_original_patterns, _original_fitnesses, ))
        _sorted_zip = sorted(_zipped, key=lambda x: x[1], reverse=True)
        # max_fitness = _sorted_zip[0][1]
        _new_individuals_pattern: [str] = []
        _new_individuals_fitness: [int] = []
        for item in _sorted_zip:
            # if item[1] < max_fitness: break
            _new_individuals_pattern.append(item[0])
            _new_individuals_fitness.append(item[1])

        self._patterns_list = _new_individuals_pattern
        self._fitness_list = _new_individuals_fitness

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

    def extract_max_patterns(self, best_percentage: float):
        self.sort()
        max_fitness = self.get_fitness_values()[0]
        _new_individuals_pattern: [str] = []
        _new_individuals_fitness: [int] = []
        for item_index in range(self.get_population_size()):
            if self._fitness_list[item_index] < max_fitness:
                break
            _new_individuals_pattern.append(self._patterns_list[item_index])
            _new_individuals_fitness.append(self._fitness_list[item_index])

        return Population(initial_goal=self._goal,
                          initial_patterns_list=_new_individuals_pattern, initial_fitness_list=_new_individuals_fitness,
                          )

    @staticmethod
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


# @staticmethod
def mutate_population(initial_population: Population, new_pop_size: int, goal: str,
                      best_percentage_mutation: float) -> Population:
    _new_best_population: Population = initial_population.extract_best_patterns( best_percentage=best_percentage_mutation)
    # _new_best_population: Population = initial_population.extract_max_patterns(
    # best_percentage=best_percentage_mutation)

    while _new_best_population.get_population_size() < new_pop_size:
        _chosen_for_mutation: str = _new_best_population.get_random_individual()[0]
        _generated_pattern: str = Mastermind.mutate(input=_chosen_for_mutation)

        _new_best_population.add_individual(pattern=_generated_pattern,
                                            fitness=Mastermind.fitness(goal=goal, curr=_generated_pattern))
    return _new_best_population


def crossover_population(initial_population: Population, new_pop_size: int, goal: str,
                         best_percentage_mutation: float) -> Population:
    _new_best_population: Population = initial_population.extract_best_patterns(
        best_percentage=best_percentage_mutation)
    # _new_best_population: Population = initial_population.extract_max_patterns(
    # best_percentage=best_percentage_mutation)

    while _new_best_population.get_population_size() < new_pop_size:
        _chosen_for_mutation_a: str = _new_best_population.get_random_individual()[0]
        _chosen_for_mutation_b: str = _new_best_population.get_random_individual()[0]
        _generated_pattern: str = Mastermind.crossover(input_a=_chosen_for_mutation_a, input_b=_chosen_for_mutation_b)

        _new_best_population.add_individual(pattern=_generated_pattern,
                                            fitness=Mastermind.fitness(goal=goal, curr=_generated_pattern))
    return _new_best_population
