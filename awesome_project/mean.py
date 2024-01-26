from .sum import add_all
from typing import Iterable


def take_average(xs: Iterable):
    n = len(xs)
    return add_all(xs) / n