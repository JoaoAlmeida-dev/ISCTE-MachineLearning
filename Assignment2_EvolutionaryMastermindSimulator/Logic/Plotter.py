from statistics import mean

from matplotlib import pyplot as plt

from Assignment2_EvolutionaryMastermindSimulator.Exercises.Constants import BITS
from Assignment2_EvolutionaryMastermindSimulator.Logic.Result import Result


def plot_results_list(results: [[Result]], title: str):
    attempts_list = [[] for _ in range(len(BITS))]
    run_time_list = [[] for _ in range(len(BITS))]
    pattern_size_list = [[] for _ in range(len(BITS))]
    # successfull_list = [[] for _ in range(len(bits))]
    for pattern_size in results:
        for result in pattern_size:
            attempts_list[BITS.index(result.pattern_size)].append(result.attempts)
            run_time_list[BITS.index(result.pattern_size)].append(result.run_time)
            pattern_size_list[BITS.index(result.pattern_size)].append(result.pattern_size)
            # successfull_list[bits.index(result.pattern_size)].append(result.successfull)

    mean_attempts_list = []
    for attempt in attempts_list:
        mean_attempts_list.append(mean(attempt))
    mean_run_times_list = []
    for run_time in run_time_list:
        mean_run_times_list.append(mean(run_time))

    plt.subplot(2, 1, 1)
    plt.title(title + " attempts/generations")
    plt.plot(BITS, mean_attempts_list, )
    plt.boxplot(attempts_list, positions=BITS, notch=True)
    plt.xlabel("pattern_size")
    plt.ylabel("attempts")

    plt.subplot(2, 1, 2)
    plt.title(title + " runtimes")
    plt.plot(BITS, mean_run_times_list, )
    plt.boxplot(run_time_list, positions=BITS, notch=True)
    plt.xlabel("pattern_size")
    plt.ylabel("run_time")

    plt.tight_layout()
    plt.show()
