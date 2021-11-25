from typing import List, Tuple


class Percetron:
    blank_weight: float
    blank_weight_variance: float

    weights: List[float]
    weights_variance: List[float]
    learning_rate: float = 10E-4
    desired_results: List[Tuple[Tuple[float, float], float]]

    def __init__(self, weigths: List[float], combinations: List[Tuple[float, float]], desired_values: List[float]):
        self.blank_weight = weigths[0]
        self.blank_weight_variance = self.blank_weight
        self.weights = weigths[1::]
        self.weights_variance = weigths
        self.desired_results = []

        for combination, desired_value in zip(combinations, desired_values):
            self.desired_results.append((combination, desired_value))

    def calculate(self, combination: Tuple[float, float]) -> Tuple[Tuple[float, float], int]:
        result = self.blank_weight
        for (value, weight) in zip(combination, self.weights):
            result += value * weight

        return self._deciding_function(combination=combination, calculated_value=result)

    def calculate_all(self, list_values: List[Tuple[float, float]]) -> List[Tuple[Tuple[float, float], int]]:
        results: List[Tuple[Tuple[float, float], int]] = []
        for value_tuple in list_values:
            results.append(self.calculate(combination=value_tuple))
        return results

    def calculate_error(self, calculated_combination_value:Tuple[Tuple[float, float], int]):
        return self.desired_results[self.desired_results.index(calculated_combination_value[0])][1] - calculated_combination_value[1]

    @staticmethod
    def _deciding_function(combination: Tuple[float, float], calculated_value: float) -> Tuple[Tuple[float, float], int]:
        deciding_value: float = 0
        if calculated_value > deciding_value:
            return combination, 1
        else:
            return combination, -1

    def update_weight_variances(self, calculated_values: List[float], error: float, ) -> None:
        self.blank_weight_variance += self.learning_rate * error
        for index in range(min(len(self.weights_variance), len(calculated_values))):
            self.weights_variance[index] += self.learning_rate * calculated_values[index][1] * error

    def update_weights(self) -> None:
        self.blank_weight += self.blank_weight_variance

        for (weight, weight_variance) in zip(self.weights, self.weights_variance):
            weight += weight_variance
