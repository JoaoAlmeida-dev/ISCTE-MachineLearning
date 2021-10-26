import concurrent.futures
import random
import threading
import timeit

from matplotlib import pyplot as plt

from Assignment2_EvolutionaryMastermindSimulator.Exercises.Constants import TRIAL_RUNS, bits, TIME_LIMIT
from Assignment2_EvolutionaryMastermindSimulator.Logic.Plotter import plot_results_list
from Assignment2_EvolutionaryMastermindSimulator.Logic.Mastermind import Mastermind
from Assignment2_EvolutionaryMastermindSimulator.Logic.Result import Result


def _assignment2_exercise2_line_a():
    def demo1():
        _goal = "0000"
        current_solution: str = Mastermind.randomBitPattern(size=len(_goal))
        mutated: str = Mastermind.mutate(input=current_solution)
        print("Assignment2_EvolutionaryMastermindSimulator::Exercise2::line_a::_goal", _goal,
              "\ncurrent_solution:", current_solution,
              "fitness:", Mastermind.fitness(goal=_goal, curr=current_solution),
              "\nmutate:", mutated,
              "fitness_mutated:", Mastermind.fitness(goal=_goal, curr=mutated),

              )

    def demo_graph():
        results: [[Result]] = [[] for _ in range(len(bits))]
        #fitnesses_list: [int] = [[] for _ in range(len(bits))]

        def randomTest(pattern_size: int):
            _goal = Mastermind.randomBitPattern(pattern_size)
            _current_pattern = Mastermind.randomBitPattern(pattern_size)
            _results_attempts: int = 0
            success = True

            _results_start = timeit.default_timer()
            while _current_pattern != _goal:
                if timeit.default_timer() - _results_start > TIME_LIMIT:
                    success = False
                    result = Result(run_time=timeit.default_timer() - _results_start, attempts=_results_attempts,
                                    pattern_size=pattern_size,
                                    successfull=success)
                    _store_result(result)
                    return result
                _original_fitness = Mastermind.fitness(goal=_goal, curr=_current_pattern)
                _counter: int = 0
                _mutated: str = _current_pattern
                while Mastermind.fitness(goal=_goal, curr=_mutated) <= _original_fitness and _counter < 1000:
                    _mutated = Mastermind.mutate(_current_pattern)
                    _results_attempts += 1
                    _counter += 1
                _current_pattern = _mutated
                # print("Assignment2::Exercise2::demo_graph::randomTest::goal:",_goal,"current:",_current_pattern)
                #fitnesses_list[bits.index(pattern_size)].append(Mastermind.fitness(goal=_goal, curr=_mutated))
            _results_stop = timeit.default_timer()

            result = Result(
                run_time=_results_stop - _results_start,
                attempts=_results_attempts,
                pattern_size=pattern_size,
                successfull=success,
            )
            _store_result(result)

        def _store_result(result: Result):
            lock.acquire()

            results[bits.index(result.pattern_size)].append(result)
            print("Assignment2_EvolutionaryMastermindSimulator::Exercise2::ThreadN:",threading.get_ident(),"::_store_result::\t" + str(result))  # str(result.__dict__))
            lock.release()

        with concurrent.futures.ThreadPoolExecutor() as executor:
            # [executor.submit(randomTest,bit) for bit in bits]
            for _ in range(TRIAL_RUNS):
                executor.map(randomTest, bits)
        plot_results_list(results=results)

    demo1()
    demo_graph()


if __name__ == '__main__':
    lock = threading.Lock()
    random.seed(1)
    _assignment2_exercise2_line_a()
