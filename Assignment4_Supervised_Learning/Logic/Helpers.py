from random import random
from typing import List, Tuple

from Assignment4_Supervised_Learning.Models.Flower import Flower


def random_split_dataset(dataset: List[Flower]) -> Tuple[List[Flower], List[Flower]]:
    dataset1: List[Flower] = []
    dataset2: List[Flower] = []
    dataset_copy = dataset.copy()
    counter: int = 0
    max_len_dataset1 = int(len(dataset_copy) * 0.7)
    max_len_dataset2 = int(len(dataset_copy) * 0.3)
    while len(dataset_copy) > 0:
        random_index: int = int(random() * len(dataset_copy))
        if counter <= max_len_dataset1:
            dataset1.append(dataset_copy.pop(random_index))
        else:
            dataset2.append(dataset_copy.pop(random_index))
        counter += 1
    return dataset1, dataset2