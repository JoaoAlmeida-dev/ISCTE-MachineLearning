import concurrent.futures
import random
import threading
import timeit

from matplotlib import pyplot as plt

from Assignment2_EvolutionaryMastermindSimulator.Exercises.Constants import TRIAL_RUNS, BITS, TIME_LIMIT
from Assignment2_EvolutionaryMastermindSimulator.Exercises.Thread_Launcher import launch_Threads, store_result
from Assignment2_EvolutionaryMastermindSimulator.Logic.Plotter import plot_results_list
from Assignment2_EvolutionaryMastermindSimulator.Logic.Mastermind import Mastermind
from Assignment2_EvolutionaryMastermindSimulator.Logic.Result import Result


def demo1():
    _goal = "0000"
    current_solution: str = Mastermind.random_bit_pattern(size=len(_goal))
    mutated: str = Mastermind.mutate(input=current_solution)
    print("Assignment2_EvolutionaryMastermindSimulator::Exercise2::line_a::_goal", _goal,
          "\ncurrent_solution:", current_solution,
          "fitness:", Mastermind.fitness(goal=_goal, curr=current_solution),
          "\nmutate:", mutated,
          "fitness_mutated:", Mastermind.fitness(goal=_goal, curr=mutated),

          )


def _assignment2_exercise2_line_a(pattern_size: int):
    _goal = Mastermind.random_bit_pattern(pattern_size)
    _current_pattern = Mastermind.random_bit_pattern(pattern_size)
    _results_attempts: int = 0
    _success = True

    _results_start = timeit.default_timer()
    while _current_pattern != _goal:
        if timeit.default_timer() - _results_start > TIME_LIMIT:
            _success = False
            result = Result(run_time=timeit.default_timer() - _results_start, attempts=_results_attempts,
                            pattern_size=pattern_size,
                            successfull=_success)
            store_result(result=result, results=exercise2_results_list, lock=exercise2_lock)
            return
        else:
            _original_fitness = Mastermind.fitness(goal=_goal, curr=_current_pattern)
            _counter: int = 0
            _mutated: str = _current_pattern
            while Mastermind.fitness(goal=_goal, curr=_mutated) <= _original_fitness and _counter < 1000:
                _mutated = Mastermind.mutate(_current_pattern)
                _results_attempts += 1
                _counter += 1
            _current_pattern = _mutated
        # print("Assignment2::Exercise2::demo_graph::randomTest::goal:",_goal,"current:",_current_pattern)
        # fitnesses_list[bits.index(pattern_size)].append(Mastermind.fitness(goal=_goal, curr=_mutated))
    if _success:
        _results_stop = timeit.default_timer()
        result = Result(
            run_time=_results_stop - _results_start,
            attempts=_results_attempts,
            pattern_size=pattern_size,
            successfull=_success,
        )
        store_result(result=result, results=exercise2_results_list, lock=exercise2_lock)


if __name__ == '__main__':
    random.seed(1)
    exercise2_lock = threading.Lock()
    exercise2_results_list: [[Result]] = [[] for _ in range(len(BITS))]
    launch_Threads(method_to_run=_assignment2_exercise2_line_a, results=exercise2_results_list)
    plot_results_list(results=exercise2_results_list, title="Exercise2")
