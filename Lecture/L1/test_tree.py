from Tree import Tree

import pytest


@pytest.fixture
def tree():
    return Tree()

@pytest.mark.parametrize(
    "arr, expected",
    [
        ([1, 2, 3, 4, 5], 4),
        ([5, 4, 3, 2, 1], 4),
        ([1, 3, 6], 5),       # 2 + 3 = 5
        ([10, 10], 0),        # расстояние 0
        ([0, -2, -5], 5),     # 2 + 3 = 5
        ([3], 0),
        ([], 0),
        ([5, 5, 5], 0),
    ]
)
def test_garland_length(arr, expected):
    tree = Tree()
    res = tree.garland_length(arr)
    assert res == expected


