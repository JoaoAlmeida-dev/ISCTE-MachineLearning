import random


def randomBitPattern(size: int) -> str:
    result: str = ""
    for i in range(size):
        if random.random() > 0.5:
            result += '0'
        else:
            result += '1'

    return result
