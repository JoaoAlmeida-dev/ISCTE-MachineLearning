import math
from pathlib import Path
from typing import List, Tuple

from Assignment4_Supervised_Learning.Logic.Loader import loadData
from Assignment4_Supervised_Learning.Models.Flower import Flower, FlowerEnum


def mean_collumn_dataset(collumn: int, dataset: List[Flower]) -> float:
    if dataset:
        sum_of_collumn: float = 0
        for flower in dataset:
            sum_of_collumn += flower[collumn]
        return sum_of_collumn / len(dataset)
    else:
        return 0


def split_dataset_based_on_collumn(dataset: List[Flower], collumn: int) -> Tuple[List[Flower], List[Flower]]:
    mean: float = mean_collumn_dataset(dataset=dataset, collumn=collumn)
    upper_list: List[Flower] = []
    lower_list: List[Flower] = []
    for flower in dataset:
        if flower[collumn] >= mean:
            upper_list.append(flower)
        else:
            lower_list.append(flower)
    return upper_list, lower_list


def calculate_percentage_str(dataset: List[Flower], flr_class: FlowerEnum) -> float:
    if dataset:
        counter: int = 0
        for flower in dataset:
            if flower.flower_class == flr_class:
                counter += 1
        return counter / len(dataset)
    else:
        return 0


def calculate_entropy(pplus: float) -> float:
    if pplus > 0:
        pminus = 1 - pplus
        return -pplus * math.log2(pplus) - pminus * math.log2(pminus)
    else:
        return 0


def calculate_set_entropy(dataset: List[Flower], flr_class: FlowerEnum):
    pplus = calculate_percentage_str(dataset=dataset, flr_class=flr_class)
    return calculate_entropy(pplus=pplus)


def calculate_gain(dataset: List[Flower], feature: int, flr_class: FlowerEnum):
    upper_split, lower_split = split_dataset_based_on_collumn(dataset=dataset, collumn=feature)

    original_set_entropy: float = calculate_set_entropy(dataset=dataset, flr_class=flr_class)
    upper_set_entropy: float = calculate_set_entropy(dataset=upper_split, flr_class=flr_class)
    lower_set_entropy: float = calculate_set_entropy(dataset=lower_split, flr_class=flr_class)

    sum_len_times_entropy = len(upper_split) * upper_set_entropy + len(lower_split) * lower_set_entropy
    gain = original_set_entropy - sum_len_times_entropy / len(dataset)
    return gain


def calculate_gains_all_features(dataset: List[Flower], flr_class: FlowerEnum) -> Tuple[int, float]:
    gain_list: List[float] = []
    for feature in range(4):
        gain_list.append(calculate_gain(dataset=dataset, feature=feature, flr_class=flr_class))
    print(gain_list)
    max_index:int =gain_list.index(max(gain_list))
    return max_index, gain_list[max_index]


if __name__ == '__main__':
    root_path = Path(__file__).parent.parent
    flowers: List[Flower] = loadData(str(root_path) + "/Resources/iris.data")
    upper_list, lower_list = split_dataset_based_on_collumn(flowers, 0)
    print(upper_list)
    print(lower_list)

    print("upper_list entropy=", calculate_set_entropy(dataset=upper_list, flr_class=FlowerEnum.Iris_setosa))
    print("lower_list entropy=", calculate_set_entropy(dataset=lower_list, flr_class=FlowerEnum.Iris_setosa))
    print("gain", calculate_gain(dataset=flowers, feature=0, flr_class=FlowerEnum.Iris_setosa))
    print("All_gains", calculate_gains_all_features(dataset=flowers, flr_class=FlowerEnum.Iris_setosa))
