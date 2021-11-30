from pathlib import Path
from typing import List, Tuple

from Assignment4_Supervised_Learning.Logic.Helpers import random_split_dataset
from Assignment4_Supervised_Learning.Logic.Loader import loadData
from Assignment4_Supervised_Learning.Models.Flower import Flower, FlowerEnum


def max_min_features(dataset: List[Flower]):
    max_values: List[float] = [
        dataset[0].petal_width,
        dataset[0].petal_length,
        dataset[0].sepal_width,
        dataset[0].sepal_length,
    ]
    min_values: List[float] = [
        dataset[0].petal_width,
        dataset[0].petal_length,
        dataset[0].sepal_width,
        dataset[0].sepal_length,
    ]

    for flower in dataset:
        if flower.petal_width > max_values[0]: max_values[0] = flower.petal_width
        if flower.petal_length > max_values[1]: max_values[1] = flower.petal_length
        if flower.sepal_width > max_values[2]: max_values[2] = flower.sepal_width
        if flower.sepal_length > max_values[3]: max_values[3] = flower.sepal_length

        if flower.petal_width < min_values[0]: min_values[0] = flower.petal_width
        if flower.petal_length < min_values[1]: min_values[1] = flower.petal_length
        if flower.sepal_width < min_values[2]: min_values[2] = flower.sepal_width
        if flower.sepal_length < min_values[3]: min_values[3] = flower.sepal_length
    return max_values, min_values


# region bins

def create_bins() -> List[Tuple[int, int]]:
    # return [(0, 1), (1,2), (2, 3), (3, 4),(4, 5), (5, 6), (6, 7), (7, 8)]
    return [(0, 2), (2, 4), (4, 6), (6, 8)]


def put_flower_in_bin(flower_feature: float, bins: List[Tuple[int, int]]) -> int:
    for bin_index, bin in enumerate(bins):
        if bin[0] <= flower_feature < bin[1]:
            return bin_index
    return -1


def binned_set(dataset: List[Flower], bins: List[Tuple[int, int]], features_n=4):
    organized_set: List[List[List[Flower]]] = [[[] for _ in bins] for _ in range(features_n)]
    for flower in dataset:
        for feature_index in range(features_n):
            calculated_bin: int = put_flower_in_bin(flower_feature=flower[feature_index], bins=bins)
            organized_set[feature_index][calculated_bin].append(flower)
    return organized_set


def new_binned_set(dataset: List[Flower], bins: List[Tuple[int, int]]) -> List[Tuple[int, int, int, int, FlowerEnum]]:
    binned_flowers: List[Tuple[int, int, int, int, FlowerEnum]] = []
    for flower in dataset:
        new_binned_flower: Tuple[int, int, int, int, FlowerEnum] = (
            put_flower_in_bin(flower_feature=flower[0], bins=bins),
            put_flower_in_bin(flower_feature=flower[1], bins=bins),
            put_flower_in_bin(flower_feature=flower[2], bins=bins),
            put_flower_in_bin(flower_feature=flower[3], bins=bins),
            flower.flower_class
        )
        binned_flowers.append(new_binned_flower)
    return binned_flowers

def organize_binned_set_by_flowerenum(binned_set:List[Tuple[int, int, int, int, FlowerEnum]] )-> List[List[Tuple[int, int, int, int, FlowerEnum]]]:
    flower_enums:List[FlowerEnum] = [ i for i in FlowerEnum]
    organized_binned_set:List[List[Tuple[int, int, int, int, FlowerEnum]]] = [ [] for _ in FlowerEnum]
    for flower in binned_set:
        organized_binned_set[flower_enums.index(flower[-1])].append(flower)


    return organized_binned_set




# endregion

# region probabilities

def calculate_probability_matrix(dataset: List[Flower], bins: List[Tuple[int, int]], features_n=4):
    len_dataset = len(dataset)
    probability_matrix: List[List[List[Flower]]] = [[[] for _ in bins] for _ in range(features_n)]
    organized_set = binned_set(dataset=dataset, bins=bins, features_n=features_n)
    for row_index in range(len(organized_set)):
        for collumn_index in range(len(organized_set[row_index])):
            flower_n = len(organized_set[row_index][collumn_index])
            probability = flower_n / len_dataset
            probability_matrix[row_index][collumn_index] = probability
    print(probability_matrix)


def calculate_probability_class_in_dataset(new_class: FlowerEnum, dataset: List[Flower]):
    if dataset:
        counter: int = 0
        for flower in dataset:
            if flower.flower_class == new_class:
                counter += 1
        return counter / len(dataset)
    else:
        return 0

# endregion

def guess_new_entry(new_entry: Flower, training_set: List[Flower], features_n=4):
    _bins = create_bins()
    probability_new_class: float = calculate_probability_class_in_dataset(new_class=new_entry.flower_class,
                                                                          dataset=training_set)
    _binned_set = new_binned_set(dataset=training_set, bins=bins)
    organize_binned_set_by_flowerenum(binned_set=_binned_set)
    print()


if __name__ == '__main__':
    root_path = Path(__file__).parent.parent
    bins = create_bins()
    print(root_path)
    flowers: List[Flower] = loadData(str(root_path) + "/Resources/iris.data")
    training_set, test_set = random_split_dataset(flowers)
    max_values, min_values = max_min_features(flowers)
    print("max", max_values, "min", min_values)
    binned_set(dataset=flowers, bins=bins)
    calculate_probability_matrix(dataset=flowers, bins=bins)
    guess_new_entry(new_entry=test_set[0], training_set=training_set)
