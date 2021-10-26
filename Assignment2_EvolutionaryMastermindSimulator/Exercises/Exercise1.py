import concurrent.futures
import random
import threading
import timeit

from Assignment2_EvolutionaryMastermindSimulator.Exercises.Constants import TIME_LIMIT, TRIAL_RUNS, bits
from Assignment2_EvolutionaryMastermindSimulator.Logic.Mastermind import Mastermind
from Assignment2_EvolutionaryMastermindSimulator.Logic.Plotter import plot_results_list
from Assignment2_EvolutionaryMastermindSimulator.Logic.Result import Result


def _assignment2_exercise1_line_a():
    print("Exercise1::LineA::", Mastermind.randomBitPattern(size=10))
    print("Exercise1::LineA::", Mastermind.randomBitPattern(size=10))
    print("Exercise1::LineA::", Mastermind.randomBitPattern(size=10))


def _assignment2_exercise1_line_b():
    results: [[Result]] = [[] for _ in range(len(bits))]

    def randomTest(patternSize: int) -> Result:
        pattern: str = Mastermind.randomBitPattern(size=patternSize)
        generated_pattern: str = ""

        start = timeit.default_timer()
        attempts = 0
        success: bool = False
        while pattern != generated_pattern:
            generated_pattern = Mastermind.randomBitPattern(size=patternSize)
            if timeit.default_timer() - start > TIME_LIMIT:
                success = False
                result = Result(run_time=timeit.default_timer() - start, attempts=attempts, pattern_size=patternSize,
                                successfull=success)
                _store_result(result)
                return result

            attempts += 1
        success = True
        stop = timeit.default_timer()
        time: float = stop - start

        result = Result(run_time=time, attempts=attempts, pattern_size=patternSize, successfull=success)
        _store_result(result)
        return result

    def _store_result(result: Result):
        lock.acquire()

        results[bits.index(result.pattern_size)].append(result)
        # print("Assignment2_EvolutionaryMastermindSimulator::Exercise1::_store_result::" + str(result.__dict__))
        lock.release()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # [executor.submit(randomTest,bit) for bit in bits]
        for _ in range(TRIAL_RUNS):
            executor.map(randomTest, bits)

    plot_results_list(results=results)


def _assignment2_exercise1_line_c():
    def demo():
        goal = "0000"
        current_solution = Mastermind.randomBitPattern(size=len(goal))
        print("Assignment2_EvolutionaryMastermindSimulator::Exercise1::line_c::goal", goal, "current_solution:",
              current_solution, "evaluate:",
              Mastermind.evaluate(goal=goal, curr=current_solution))

    for _ in range(10): demo()


def _assignment2_exercise1_line_d():
    def demo():
        goal = "0000"
        current_solution = Mastermind.randomBitPattern(size=len(goal))
        print("Assignment2_EvolutionaryMastermindSimulator::Exercise1::line_c::goal", goal,
              "current_solution:", current_solution,
              "fitness:",  Mastermind.fitness(goal=goal, curr=current_solution))

    for _ in range(10): demo()


if __name__ == '__main__':
    lock = threading.Lock()
    random.seed(1)
    _assignment2_exercise1_line_a()
    print()
    _assignment2_exercise1_line_b()
    print()
    _assignment2_exercise1_line_c()
    print()
    _assignment2_exercise1_line_d()
