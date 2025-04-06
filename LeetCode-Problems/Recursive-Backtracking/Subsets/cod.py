def subsets(nums: list[int]) -> list[list[int]]:
    n = len(nums)
    ans, sol = [], []

    def backtrack(i):
        if i == n:
            ans.append(sol[:])
            return

        # Don't pick nums[i]
        backtrack(i + 1)

        # Pick nums[i]
        sol.append(nums[i])
        backtrack(i + 1)
        sol.pop()

    backtrack(0)
    return ans