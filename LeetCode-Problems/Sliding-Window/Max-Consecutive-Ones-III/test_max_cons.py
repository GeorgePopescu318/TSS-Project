import pytest
from max_cons import Solution  # Assuming the code is saved in solution.py

@pytest.mark.parametrize("nums, k, expected", [
    ([1,1,0,0,1,1,1,0,1,1], 2, 8),  # Test alternating sequence with enough k
    ([1,0,1,0,1,0,0,1,1], 3, 8),    # Test with k greater than number of zeros
    ([0,0,0,0], 2, 2),              # Test all zeros with k less than their count
    ([1,1,1,1], 1, 4),              # Test no zeros to require flips
    ([0,1,0,1,1,0,0,1], 1, 4),      # Test limited flips in alternating sequence
    ([0,0,1,1,1,1,0,0,1,0,1,1], 2, 8),  # Test with isolated ones
    ([1], 0, 1),                    # Single-element test with zero flips allowed
    ([0], 0, 0),                    # Single-element zero test with zero flips
    ([0,0,1], 3, 3),                # More flips possible than zeros available
    ([], 2, 0),                     # Empty nums list
])
def test_longestOnes(nums, k, expected):
    solution = Solution()
    assert solution.longestOnes(nums, k) == expected

# Use this command to run the tests
# pytest solution.py
