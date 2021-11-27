import random
from statistics import mean, stdev

from typing import List, Tuple

from Assignment4_Supervised_Learning.Logic.Percetron import Percetron

BITCOMBINATIONS: List[Tuple[float, float]] = [(-1, -1), (-1, 1), (1, -1), (1, 1), ]
OR_DESIRED: List[float] = [-1, 1, 1, 1]
AND_DESIRED: List[float] = [-1, -1, -1, 1]


def line1():
    print("LINE1::BITCOMBINATIONS:", BITCOMBINATIONS)
    print("LINE1::OR_DESIRED:", OR_DESIRED)
    print("LINE1::AND_DESIRED:", AND_DESIRED)


def line2(percetron: Percetron) \
        -> List[Tuple[Tuple[float, float], float]]:
    """Initialize w0, w1, and w2 to small random values and, for each input pattern calculate the output (o)."""
    print("LINE2::weights", percetron.blank_weight, percetron.weights)
    _calculated_values: List[Tuple[Tuple[float, float], float]] = []
    for combination in BITCOMBINATIONS:
        _calculated_values.append(percetron.calculate(combination))
    print("LINE2::calculated_values", _calculated_values)
    return _calculated_values


def line3(percetron: Percetron, calulated_values: List[Tuple[Tuple[float, float], float]]) \
        -> List[Tuple[Tuple[float, float], float]]:
    """Calculate the difference / error (e) between o and the desired response (d) for each output."""
    errors = percetron.calculate_error_all(calulated_values)
    print("LINE3::errors", errors)
    return errors


def line4(percetron: Percetron, errors: List[Tuple[Tuple[float, float], float]],
          calulated_values: List[Tuple[Tuple[float, float], float]]):
    """
    Add to the update term for w1 (∆w1) and w2 (∆w2) according to:
        ∆w0 = ∆w0 + α ·(d −o);
        ∆w1 = ∆w1 + α ·x1 ·(d −o);
    """
    for error in errors:
        percetron.update_weight_variances(error=error)
    print("LINE4::weights_variance", percetron.blank_weight_variance, percetron.weights_variance)


def line5(percetron: Percetron):
    """After all examples are presented (an epoch), update w1 and w2 according to:
        w0 = w0 + ∆w0 ;
        w1 = w1 + ∆w1 ;
        w2 = w2 + ∆w2 ;
        so that in the next iteration the error will diminish.
    """
    percetron.update_weights()
    print("LINE5::weights", percetron.blank_weight, percetron.weights)


def linea(percetron: Percetron, combinations: List[Tuple[float, float]], print_bool: bool):
    calculated_list: List[Tuple[Tuple[float, float], float]] = []

    errors_dont_exist: bool = False
    counter = 0
    while not errors_dont_exist:
        # while there are still errors in the calculated results
        error_check = True
        calculated_list: List[Tuple[Tuple[float, float], float]] = percetron.calculate_all(combinations)
        errors_list = percetron.calculate_error_all(calculated_combination_value_list=calculated_list)

        for error_tuple in errors_list:
            error_check = error_check and (error_tuple[1] == 0)
        if error_check:
            errors_dont_exist = True
        else:
            percetron.update_weight_variances_all(error_list=errors_list)
            percetron.update_weights()
        counter += 1

    if print_bool: print("LINEA::counter=", counter, "percetron=", percetron, )
    return counter


def lineaExperiments(input_combinations: List[Tuple[float, float]], input_desired_values: List[float],
                     learning_rate: float):
    counter_list: List[int] = []
    for _ in range(30):
        random_weights: List[float] = [random.random(), random.random(), random.random(), ]
        percetron: Percetron = Percetron(weights=random_weights, combinations=input_combinations,
                                         desired_values=input_desired_values, learning_rate=learning_rate)
        counter_list.append(linea(percetron=percetron, combinations=input_combinations, print_bool=False))
        print("LINEA_Experiments:: random_weights=", random_weights)

    _mean_counter = mean(counter_list)
    _stdev_counter = stdev(counter_list)
    return _mean_counter, _stdev_counter


def lineb(tries: int, max_learning_rate: int, input_combinations: List[Tuple[float, float]],
          input_desired_values: List[float]):
    for _ in range(tries):
        _learning_rate_lineb = random.random() * max_learning_rate
        _mean_counter, _stdev_counter = lineaExperiments(input_combinations=input_combinations,
                                                         input_desired_values=input_desired_values,
                                                         learning_rate=_learning_rate_lineb)


    pass


if __name__ == '__main__':
    example_weights: list = [0.1, 0.1, 0.1]
    example_learningrate = 10E-4

    example_or_Percetron: Percetron = Percetron(weights=example_weights, combinations=BITCOMBINATIONS,
                                                desired_values=OR_DESIRED, learning_rate=example_learningrate)
    example_and_Percetron: Percetron = Percetron(weights=example_weights, combinations=BITCOMBINATIONS,
                                                 desired_values=AND_DESIRED, learning_rate=example_learningrate)

    line1()
    _calculated_values_or = line2(example_or_Percetron)
    _calculated_values_and = line2(example_and_Percetron)

    _errors_or = line3(example_or_Percetron, _calculated_values_or)
    _errors_and = line3(example_and_Percetron, _calculated_values_and)

    line4(example_or_Percetron, errors=_errors_or, calulated_values=_calculated_values_or)
    line4(example_and_Percetron, errors=_errors_and, calulated_values=_calculated_values_and)

    line5(example_or_Percetron)
    line5(example_and_Percetron)
    print("MAIN::example_or_Percetron expected result=\t", example_or_Percetron.desired_results)
    linea(percetron=example_or_Percetron, combinations=BITCOMBINATIONS, print_bool=True)
    print("MAIN::example_and_Percetron expected result=\t", example_and_Percetron.desired_results)
    linea(percetron=example_and_Percetron, combinations=BITCOMBINATIONS, print_bool=True)

    mean_counter_or, stdev_counter_or = lineaExperiments(input_combinations=BITCOMBINATIONS,
                                                         input_desired_values=OR_DESIRED,
                                                         learning_rate=example_learningrate)
    mean_counter_and, stdev_counter_and = lineaExperiments(input_combinations=BITCOMBINATIONS,
                                                           input_desired_values=AND_DESIRED,
                                                           learning_rate=example_learningrate)

    print("LINEA_Experiments:: or mean(counter_list)=", round(mean_counter_or, 2),
          "stdev(counter_list)", round(stdev_counter_or, 2))
    print("LINEA_Experiments:: and mean(counter_list)=", round(mean_counter_and, 2),
          "stdev(counter_list)", round(stdev_counter_and, 2))
