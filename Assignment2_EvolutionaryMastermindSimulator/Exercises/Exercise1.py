import concurrent.futures
import random
import threading
import timeit
from statistics import mean

from matplotlib import pyplot as plt

from Assignment2_EvolutionaryMastermindSimulator.Logic.Mastermind import Mastermind
from Assignment2_EvolutionaryMastermindSimulator.Logic.Result import Result

TIME_LIMIT = 2  # seconds
TRIAL_RUNS = 30
bits = [2, 4, 8, 12, 16, 20, 24, 28, 32, ]


def _assignment2_exercise1_line_a():
    print("Exercise1::LineA::", Mastermind.randomBitPattern(size=10))
    print("Exercise1::LineA::", Mastermind.randomBitPattern(size=10))
    print("Exercise1::LineA::", Mastermind.randomBitPattern(size=10))


def _assignment2_exercise1_line_b():
    results: [Result] = [[] for _ in range(len(bits))]

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

    plot_results_exercise1_lineb(results=results)


def plot_results_exercise1_lineb(results: [[Result]]):
    attempts_list = [[] for _ in range(len(bits))]
    run_time_list = [[] for _ in range(len(bits))]
    pattern_size_list = [[] for _ in range(len(bits))]
    # successfull_list = [[] for _ in range(len(bits))]
    for pattern_size in results:
        for result in pattern_size:
            attempts_list[bits.index(result.pattern_size)].append(result.attempts)
            run_time_list[bits.index(result.pattern_size)].append(result.run_time)
            pattern_size_list[bits.index(result.pattern_size)].append(result.pattern_size)
            # successfull_list[bits.index(result.pattern_size)].append(result.successfull)

    mean_attempts_list = []
    for attempt in attempts_list:
        mean_attempts_list.append(mean(attempt))
    mean_run_times_list = []
    for run_time in run_time_list:
        mean_run_times_list.append(mean(run_time))

    plt.subplot(2, 1, 1)
    plt.plot(bits, mean_attempts_list, )
    plt.boxplot(attempts_list, positions=bits, notch=True)
    plt.xlabel("pattern_size")
    plt.ylabel("attempts")
    plt.subplot(2, 1, 2)
    plt.plot(bits, mean_run_times_list, )
    plt.boxplot(run_time_list, positions=bits, notch=True)
    plt.xlabel("pattern_size")
    plt.ylabel("run_time")
    plt.tight_layout()
    plt.show()


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
