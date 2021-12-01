from typing import List, Tuple


class Percetron:
    blank_weight: float
    blank_weight_variance: float

    weights: List[float]
    weights_variance: List[float]
    learning_rate: float
    desired_results: List[Tuple[Tuple[float, float], float]]

    def __init__(self, weights: List[float], combinations: List[Tuple[float, float]], desired_values: List[float],
                 learning_rate: float):
        self.blank_weight = weights[0]
        self.blank_weight_variance = 0
        self.weights = weights[1::]
        self.weights_variance = [0 for _ in self.weights]
        self.desired_results = []
        self.learning_rate = learning_rate

        for combination, desired_value in zip(combinations, desired_values):
            self.desired_results.append((combination, desired_value))

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return self.__str__()

    def set_weights(self, weights: List[float]):
        self.blank_weight = weights[0]
        self.weights = weights[1::]
        self.weights_variance = self.weights

    @staticmethod
    def _deciding_function(combination: Tuple[float, float], calculated_value: float) \
            -> Tuple[Tuple[float, float], float]:
        deciding_value: float = 0
        if calculated_value > deciding_value:
            return combination, 1
        else:
            return combination, -1

    def calculate(self, combination: Tuple[float, float]) \
            -> Tuple[Tuple[float, float], float]:

        result = self.blank_weight
        for (value, weight) in zip(combination, self.weights):
            result += value * weight

        return self._deciding_function(combination=combination, calculated_value=result)

    def calculate_all(self, list_values: List[Tuple[float, float]]) \
            -> List[Tuple[Tuple[float, float], float]]:

        results: List[Tuple[Tuple[float, float], float]] = []
        for value_tuple in list_values:
            results.append(self.calculate(combination=value_tuple))
        return results

    def calculate_error(self, calculated_combination_value: Tuple[Tuple[float, float], float]) \
            -> Tuple[Tuple[float, float], float]:

        index = self._desired_index(calculated_combination_value[0])
        error = self.desired_results[index][1] - calculated_combination_value[1]
        return calculated_combination_value[0], error

    def _desired_index(self, combination: Tuple[float, float]) \
            -> int:
        index = -1
        for tuple_index, tuple_value in enumerate(self.desired_results):
            if tuple_value[0][0] == combination[0] and tuple_value[0][1] == combination[1]:
                index = tuple_index
        return index

    def calculate_error_all(self, calculated_combination_value_list: List[Tuple[Tuple[float, float], float]]) \
            -> List[Tuple[Tuple[float, float], float]]:

        combination_error_list: List[Tuple[Tuple[float, float], float]] = []
        for calculated_combination_value in calculated_combination_value_list:
            combination_error_list.append(
                self.calculate_error(calculated_combination_value=calculated_combination_value))
        return combination_error_list

    def update_weight_variances(self, error: Tuple[Tuple[float, float], float], ) \
            -> None:
        self.blank_weight_variance += self.learning_rate * error[1]
        for index in range(len(self.weights_variance)):
            self.weights_variance[index] += self.learning_rate * error[0][index] * error[1]

    def update_weight_variances_all(self, error_list: List[Tuple[Tuple[float, float], float]], ) \
            -> None:
        for error in error_list:
            self.update_weight_variances(error=error)

    def update_weights(self) \
            -> None:
        self.blank_weight += self.blank_weight_variance
        self.blank_weight_variance=0

        for weight_index in range(min(len(self.weights),len(self.weights_variance))):
            self.weights[weight_index] += self.weights_variance[weight_index]
            self.weights_variance[weight_index] = 0

