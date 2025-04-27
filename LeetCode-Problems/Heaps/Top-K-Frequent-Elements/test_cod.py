import pytest
from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        counter = Counter(nums)
        buckets = [0] * (n + 1)

        for num, freq in counter.items():
            if buckets[freq] == 0:
                buckets[freq] = [num]
            else:
                buckets[freq].append(num)
        
        ret = []
        for i in range(n, -1, -1):
            if buckets[i] != 0:
                ret.extend(buckets[i])
            if len(ret) == k:
                break
        
        return ret

@pytest.fixture
def solution():
    return Solution()

def test_topKFrequent_basic_case(solution):
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    assert set(solution.topKFrequent(nums, k)) == {1, 2}

def test_topKFrequent_single_element(solution):
    nums = [1]
    k = 1
    assert solution.topKFrequent(nums, k) == [1]

def test_topKFrequent_all_unique(solution):
    nums = [1, 2, 3, 4, 5]
    k = 3
    assert set(solution.topKFrequent(nums, k)) == {1, 2, 3} #AssertionError: assert {1, 2, 3, 4, 5} == {1, 2, 3}

def test_topKFrequent_all_same(solution):
    nums = [1, 1, 1, 1]
    k = 1
    assert solution.topKFrequent(nums, k) == [1]

def test_topKFrequent_large_k(solution):
    nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    k = 3
    assert set(solution.topKFrequent(nums, k)) == {2, 3, 4}

def test_topKFrequent_k_equals_length(solution):
    nums = [1, 2, 3, 4, 5]
    k = 5
    assert set(solution.topKFrequent(nums, k)) == {1, 2, 3, 4, 5}

def test_topKFrequent_empty_list(solution):
    nums = []
    k = 0
    assert solution.topKFrequent(nums, k) == []

def test_topKFrequent_k_greater_than_unique_elements(solution):
    nums = [1, 2, 2, 3, 3, 3]
    k = 5
    assert set(solution.topKFrequent(nums, k)) == {1, 2, 3}
