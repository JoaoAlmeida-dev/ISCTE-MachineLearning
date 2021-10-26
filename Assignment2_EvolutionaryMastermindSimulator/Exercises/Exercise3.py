import concurrent.futures
import random
import threading
import timeit

from matplotlib import pyplot as plt

from Assignment2_EvolutionaryMastermindSimulator.Exercises.Constants import TRIAL_RUNS, bits, TIME_LIMIT
from Assignment2_EvolutionaryMastermindSimulator.Logic.Mastermind import Mastermind
from Assignment2_EvolutionaryMastermindSimulator.Logic.Plotter import plot_results_list
from Assignment2_EvolutionaryMastermindSimulator.Logic.Population import Population, mutate_population
from Assignment2_EvolutionaryMastermindSimulator.Logic.Result import Result

STAGNATION_VARIANCE = 0.025

#exercise3_max_generations = 100
exercise3_best_percentage = 0.3
exercise3_sample_size = 100


def _assignment2_exercise3_line_a():
    results: [[Result]] = [[] for _ in range(len(bits))]

    def randomTest(pattern_size: int):
        _goal = Mastermind.randomBitPattern(pattern_size)

        _results_generation_counter: int = 0
        _success = True

        _current_population = Population.generate_fist_population(goal=_goal, sample_size=exercise3_sample_size)
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
            _current_population = mutate_population(initial_population=_current_population,
                                                    new_pop_size=exercise3_sample_size, goal=_goal,
                                                    best_percentage_mutation=exercise3_best_percentage)
            _results_generation_counter += 1

        _results_stop = timeit.default_timer()
        result = Result(
            run_time=_results_stop - _results_start,
            attempts=_results_generation_counter,
            pattern_size=pattern_size,
            successfull=_success,
        )
        print("Assignment2_EvolutionaryMastermindSimulator::Exercise2::", threading.get_ident(),
              "population_mean_fitness", _current_population.get_mean_fitness(), "::" + str(result))
        _store_result(result)

    def _store_result(result: Result):
        lock.acquire()

        results[bits.index(result.pattern_size)].append(result)
        print("Assignment2_EvolutionaryMastermindSimulator::Exercise3::ThreadN:", threading.get_ident(),
              "::_store_result::\t" + str(result))  # str(result.__dict__))
        lock.release()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # [executor.submit(randomTest,bit) for bit in bits]
        for _ in range(TRIAL_RUNS):
            executor.map(randomTest, bits)
    plot_results_list(results=results)


if __name__ == '__main__':
    lock = threading.Lock()
    # random.seed(1)
    _assignment2_exercise3_line_a()
