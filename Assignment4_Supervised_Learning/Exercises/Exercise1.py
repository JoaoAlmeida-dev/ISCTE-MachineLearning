import random

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
    """Initialize w0, w1, and w2 to small random values and, for each input pattern calculate the output (o).
        """
    print("LINE2::weights", percetron.blank_weight, percetron.weights)
    _calculated_values: List[Tuple[Tuple[float, float], float]] = []
    for combination in BITCOMBINATIONS:
        _calculated_values.append(percetron.calculate(combination))
    print("LINE2::calculated_values", _calculated_values)
    return _calculated_values


def line3(percetron: Percetron, calulated_values: List[Tuple[Tuple[float, float], float]]) \
        -> List[Tuple[Tuple[float, float], float]]:
    """
    Calculate the difference / error (e) between o and the desired response (d) for each output.
    """
    errors = percetron.calculate_error_all(calulated_values)
    print("LINE3::errors", errors)
    return errors


def line4(percetron: Percetron, errors: List[Tuple[Tuple[float, float], float]],
          calulated_values: List[Tuple[Tuple[float, float], float]]):
    """Add to the update term for w1 (∆w1) and w2 (∆w2) according to:
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


def linea(percetron: Percetron, combinations: List[Tuple[float, float]]):
    calculated_list:List[Tuple[Tuple[float, float], float]]=[]

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

    print("LINEA::counter=", counter, "last_calculated_values=\t", calculated_list, "percetron=", percetron, )


if __name__ == '__main__':
    example_weights: list = [0.1, 0.1, 0.1]

    example_or_Percetron: Percetron = Percetron(weigths=example_weights, combinations=BITCOMBINATIONS,
                                                desired_values=OR_DESIRED)
    example_and_Percetron: Percetron = Percetron(weigths=example_weights, combinations=BITCOMBINATIONS,
                                                 desired_values=AND_DESIRED)

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
    linea(percetron=example_or_Percetron, combinations=BITCOMBINATIONS)
    print("MAIN::example_and_Percetron expected result=\t", example_and_Percetron.desired_results)
    linea(percetron=example_and_Percetron, combinations=BITCOMBINATIONS)
