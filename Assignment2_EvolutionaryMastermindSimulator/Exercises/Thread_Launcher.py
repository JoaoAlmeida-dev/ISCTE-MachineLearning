import concurrent.futures
import threading

from Assignment2_EvolutionaryMastermindSimulator.Exercises.Constants import bits, TRIAL_RUNS
from Assignment2_EvolutionaryMastermindSimulator.Logic.Plotter import plot_results_list
from Assignment2_EvolutionaryMastermindSimulator.Logic.Result import Result


def store_result(results:[Result], result: Result, lock:threading.Lock):
    lock.acquire()
    results[bits.index(result.pattern_size)].append(result)
    lock.release()

def launch_Threads(method_to_run, results:[Result]):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # [executor.submit(randomTest,bit) for bit in bits]
        for _ in range(TRIAL_RUNS):
            executor.map(method_to_run, bits)
