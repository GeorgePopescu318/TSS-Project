import pytest
from heapq import heapify, heappop, heappush

def lastStoneWeight(stones: list[int]) -> int:
    for i in range(len(stones)):
        stones[i] *= -1 # Negate to force Max Heap

    heapify(stones)

    while len(stones) > 1:
        largest = heappop(stones)
        next_largest = heappop(stones)

        if largest != next_largest:
            heappush(stones, largest - next_largest)

    return -heappop(stones) if stones else 0

@pytest.mark.parametrize("stones, expected", [
    ([2, 7, 4, 1, 8, 1], 1),  # Example case: after all collisions, one stone of weight 1 remains
    ([1], 1),                 # Single stone: the weight of the stone itself
    ([3, 3], 0),              # Two stones of equal weight: both are destroyed
    ([10, 4, 2, 10], 2),      # After collisions, one stone of weight 2 remains
    ([5, 5, 5, 5], 0),        # All stones have the same weight and are destroyed
    ([9, 3, 2, 10], 0),       # After collisions, no stones remain
    ([1, 2, 3, 4, 5, 6, 7, 8, 9], 1),  # Complex case with multiple collisions
    ([], 0),                  # No stones: result is 0
])
def test_lastStoneWeight(stones, expected):
    assert lastStoneWeight(stones) == expected
