import concurrent.futures
import random
import threading
import timeit

from Assignment2_EvolutionaryMastermindSimulator.Exercises.Constants import TIME_LIMIT, TRIAL_RUNS, bits
from Assignment2_EvolutionaryMastermindSimulator.Exercises.Thread_Launcher import store_result, launch_Threads
from Assignment2_EvolutionaryMastermindSimulator.Logic.Mastermind import Mastermind
from Assignment2_EvolutionaryMastermindSimulator.Logic.Plotter import plot_results_list
from Assignment2_EvolutionaryMastermindSimulator.Logic.Result import Result


def _assignment2_exercise1_line_a():
    print("Exercise1::LineA::", Mastermind.randomBitPattern(size=10))
    print("Exercise1::LineA::", Mastermind.randomBitPattern(size=10))
    print("Exercise1::LineA::", Mastermind.randomBitPattern(size=10))


def _assignment2_exercise1_line_b(patternSize: int):
    _goal_pattern: str = Mastermind.randomBitPattern(size=patternSize)
    _generated_pattern: str = ""

    _start = timeit.default_timer()
    _attempts = 0
    _success: bool = True
    while _goal_pattern != _generated_pattern:
        _generated_pattern = Mastermind.randomBitPattern(size=patternSize)
        #if timeit.default_timer() - _start > TIME_LIMIT:
        #    _success = False
        #    _result = Result(run_time=timeit.default_timer() - _start, attempts=_attempts, pattern_size=patternSize,
        #                     successfull=_success)
        #    store_result(result=_result, results=exercise1_results_list, lock=exercise1_lock)

        _attempts += 1
    _stop = timeit.default_timer()
    _time: float = _stop - _start

    _result = Result(run_time=_time, attempts=_attempts, pattern_size=patternSize, successfull=_success)

    #print("Assignment2_EvolutionaryMastermindSimulator::Exercise1::", threading.get_ident(),
    #      "population_mean_fitness::" + str(_result))
    store_result(result=_result, results=exercise1_results_list, lock=exercise1_lock)


def _assignment2_exercise1_line_c():
    def demo():
        _goal = "0000"
        _current_solution = Mastermind.randomBitPattern(size=len(_goal))
        print("Assignment2_EvolutionaryMastermindSimulator::Exercise1::line_c::goal", _goal, "current_solution:",
              _current_solution, "evaluate:",
              Mastermind.evaluate(goal=_goal, curr=_current_solution))

    for _ in range(10): demo()


def _assignment2_exercise1_line_d():
    def demo():
        _goal = "0000"
        _current_solution = Mastermind.randomBitPattern(size=len(_goal))
        print("Assignment2_EvolutionaryMastermindSimulator::Exercise1::line_c::goal", _goal,
              "current_solution:", _current_solution,
              "fitness:", Mastermind.fitness(goal=_goal, curr=_current_solution))

    for _ in range(10):
        demo()


if __name__ == '__main__':
    random.seed(1)
    exercise1_lock = threading.Lock()
    exercise1_results_list: [[Result]] = [[] for _ in range(len(bits))]

    _assignment2_exercise1_line_a()
    print()

    launch_Threads(method_to_run=_assignment2_exercise1_line_b, results=exercise1_results_list)
    plot_results_list(results=exercise1_results_list, title="Exercise1")

    print()
    _assignment2_exercise1_line_c()
    print()
    _assignment2_exercise1_line_d()
