import numpy as np
from typing import Iterable


def add_all(xs: Iterable):
    return np.sum(xs).item()