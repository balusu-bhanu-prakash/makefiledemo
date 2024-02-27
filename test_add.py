import numpy as np
from add import add


def test_add():
    assert np.array_equal(np.array([1, 1]), add(np.array([1, 0]), np.array([0, 1])))