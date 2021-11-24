import random

from typing import List, Tuple

from Assignment4_SUpervised_Learning.Logic.Percetron import Percetron

BITCOMBINATIONS: List[Tuple[float, float]] = [(-1, -1), (-1, 1), (1, -1), (1, 1), ]
OR_DESIRED: List[float] = [-1, 1, 1, 1]
AND_DESIRED: List[float] = [-1, -1, -1, 1]


def line1():
    print("LINE1::BITCOMBINATIONS:", BITCOMBINATIONS)
    print("LINE1::OR_DESIRED:", OR_DESIRED)
    print("LINE1::AND_DESIRED:", AND_DESIRED)


def line2(percetron: Percetron) -> List[float]:
    """Initialize w0, w1, and w2 to small random values and, for each input pattern calculate the output (o).
        """
    print("LINE2::weights", percetron.blank_weight, percetron.weights)
    _calculated_values: List[float] = []
    for combination in BITCOMBINATIONS:
        _calculated_values.append(percetron.calculate(combination))
    print("LINE2::calculated_values", _calculated_values)
    return _calculated_values


def line3(percetron: Percetron, calulated_values: List[float]) -> List[float]:
    """
    Calculate the difference / error (e) between o and the desired response (d) for each output.
    """
    errors = []
    for value, desired in zip(calulated_values, percetron.desired_values):
        errors.append(desired - value)
    print("LINE3::errors", errors)
    return errors


def line4(percetron: Percetron, errors: List[float], calulated_values: List[float]):
    """Add to the update term for w1 (∆w1) and w2 (∆w2) according to:
        ∆w0 = ∆w0 + α ·(d −o);
        ∆w1 = ∆w1 + α ·x1 ·(d −o);
    """
    for error in errors:
        percetron.update_weight_variances(calculated_values=calulated_values, error=error)
    print("LINE4::weights_variance",percetron.blank_weight_variance, percetron.weights_variance)


if __name__ == '__main__':
    example_weights: list = [0.1, 0.1, 0.1]

    example_or_Percetron: Percetron = Percetron(weigths=example_weights, desired_values=OR_DESIRED)
    example_and_Percetron: Percetron = Percetron(weigths=example_weights, desired_values=AND_DESIRED)

    line1()
    calculated_values_or = line2(example_or_Percetron)
    calculated_values_and = line2(example_and_Percetron)

    errors_or = line3(example_or_Percetron, calculated_values_or)
    errors_and = line3(example_and_Percetron, calculated_values_and)

    line4(example_or_Percetron, errors=errors_or, calulated_values=calculated_values_or)
    line4(example_and_Percetron, errors=errors_and, calulated_values=calculated_values_and)
