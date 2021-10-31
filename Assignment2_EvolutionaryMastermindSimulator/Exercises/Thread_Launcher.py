import concurrent.futures
import threading

from Assignment2_EvolutionaryMastermindSimulator.Exercises.Constants import BITS, TRIAL_RUNS
from Assignment2_EvolutionaryMastermindSimulator.Logic.Plotter import plot_results_list
from Assignment2_EvolutionaryMastermindSimulator.Logic.Result import Result


def store_result(results: [Result], result: Result, lock: threading.Lock):
    lock.acquire()
    results[BITS.index(result.pattern_size)].append(result)
    len_results_list: [int] = []
    for i in range(len(results)):
        len_results_list.append(len(results[i]))
    print(len_results_list)

    #print(len(results[0]),len(results[1]),len(results[2]),len(results[3]),len(results[4]))
    lock.release()


def launch_threads(method_to_run, results: [Result]):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # [executor.submit(randomTest,bit) for bit in bits]
        for _ in range(TRIAL_RUNS):
            executor.map(method_to_run, BITS)
