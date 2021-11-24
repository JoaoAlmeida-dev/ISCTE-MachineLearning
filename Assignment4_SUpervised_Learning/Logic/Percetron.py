from typing import List, Tuple


class Percetron:
    blank_weight: float
    blank_weight_variance: float

    weights: List[float]
    weights_variance: List[float]
    learning_rate: float = 10E-4
    desired_values: List[float]

    def __init__(self, weigths: List[float], desired_values: List[float]):
        self.blank_weight = weigths[0]
        self.blank_weight_variance=self.blank_weight
        self.weights = weigths[1::]
        self.weights_variance = weigths
        self.desired_values = desired_values

    def calculate(self, values: Tuple[float, float]) -> float:
        result = self.blank_weight
        for (value, weight) in zip(values, self.weights):
            result += value * weight

        return self._deciding_function(result)

    @staticmethod
    def _deciding_function(value: float) -> float:
        deciding_value: float = 0
        if value > deciding_value:
            return 1
        else:
            return -1

    def update_weight_variances(self, calculated_values: List[float], error: float, ) -> None:
        self.blank_weight_variance += self.learning_rate * error
        for index in range(min(len(self.weights_variance), len(calculated_values))):
            self.weights_variance[index] += self.learning_rate * calculated_values[index] * error

    def update_weights(self) -> None:
        self.blank_weight += self.blank_weight_variance

        for (weight, weight_variance) in zip(self.weights, self.weights_variance):
            weight += weight_variance
