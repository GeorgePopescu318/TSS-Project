import pytest
from heapq import heappush, heappushpop

def kClosest(points: list[list[int]], k: int) -> list[list[int]]:
    def dist(x, y):
        return x**2 + y**2

    heap = []
    for x, y in points:
        d = dist(x, y)
        if len(heap) < k:
            heappush(heap, (-d, x, y))
        else:
            heappushpop(heap, (-d, x, y))

    return [(x, y) for d, x, y in heap]

@pytest.mark.parametrize("points, k, expected", [
    ([(1, 3), (-2, 2)], 1, [(-2, 2)]),
    ([(3, 3), (5, -1), (-2, 4)], 2, [(3, 3), (-2, 4)]),
    ([(1, 1), (2, 2), (3, 3)], 3, [(1, 1), (2, 2), (3, 3)]),
    ([(1, 0), (0, 1)], 2, [(1, 0), (0, 1)]),
    ([(1, 0), (0, 1), (0, 0)], 1, [(0, 0)]),
    ([], 0, []),
    ([(1, 2), (2, 1), (3, 3)], 0, []),
    ([(1, 2), (2, 1), (3, 3)], 1, [(1, 2)]), #AssertionError: Expected [(1, 2)], but got [(2, 1)]
])
def test_kClosest(points, k, expected):
    result = kClosest(points, k)
    assert sorted(result) == sorted(expected), f"Expected {expected}, but got {result}"
