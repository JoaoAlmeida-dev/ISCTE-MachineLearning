import random
import threading
import timeit

from matplotlib import pyplot as plt

from Assignment2_EvolutionaryMastermindSimulator.Exercises.Constants import BITS, STAGNATION_VARIANCE
from Assignment2_EvolutionaryMastermindSimulator.Exercises.Thread_Launcher import launch_threads, store_result
from Assignment2_EvolutionaryMastermindSimulator.Logic.Mastermind import Mastermind
from Assignment2_EvolutionaryMastermindSimulator.Logic.Plotter import plot_results_list
from Assignment2_EvolutionaryMastermindSimulator.Logic.Population import Population, mutate_population, \
    crossover_population
from Assignment2_EvolutionaryMastermindSimulator.Logic.Result import Result

exercise3_max_generations = 100

exercise4_best_percentage = 0.3
exercise4_goal = "11111111"
exercise4_sample_size = 100


def _assignment2_exercise4_line_a(pattern_size: int):
    _goal = Mastermind.random_bit_pattern(pattern_size)

    _results_generation_counter: int = 0
    _success = True

    _current_population = Population.generate_fist_population(goal=_goal, sample_size=exercise4_sample_size)
    _fitness_history: [int] = []
    _stagnated: bool = False
    _results_start = timeit.default_timer()

    while not _stagnated and _current_population.get_mean_fitness() < len(_goal):
        # while _current_population.get_mean_fitness() < len(_goal):
        fitness_list_len: bool = len(_fitness_history) > 1
        if fitness_list_len:
            _stagnated = _fitness_history[
                             -1] + STAGNATION_VARIANCE > _current_population.get_mean_fitness() > \
                         _fitness_history[-1] - STAGNATION_VARIANCE

        _fitness_history.append(_current_population.get_mean_fitness())
        _current_population = crossover_population(initial_population=_current_population,
                                                   new_pop_size=exercise4_sample_size, goal=_goal,
                                                   best_percentage_mutation=exercise4_best_percentage)
        _results_generation_counter += 1

    _results_stop = timeit.default_timer()
    _result: Result = Result(
        run_time=_results_stop - _results_start,
        attempts=_results_generation_counter,
        pattern_size=pattern_size,
        successfull=_success,
    )
    #print("Assignment2_EvolutionaryMastermindSimulator::Exercise4::", threading.get_ident(),
    #      "population_mean_fitness", _current_population.get_mean_fitness(), "::" + str(_result))
    store_result(results=exercise4_results_list, result=_result, lock=exercise4_lock)


if __name__ == '__main__':
    random.seed(1)
    exercise4_lock = threading.Lock()
    exercise4_results_list: [[Result]] = [[] for _ in range(len(BITS))]
    launch_threads(method_to_run=_assignment2_exercise4_line_a, results=exercise4_results_list)
    plot_results_list(results=exercise4_results_list, title="Exercise4")
