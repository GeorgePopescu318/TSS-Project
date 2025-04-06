def permute(nums: list[int]) -> list[list[int]]:
    n = len(nums)
    ans, sol = [], []

    def backtrack():
        if len(sol) == n:
            ans.append(sol[:])
            return

        for x in nums:
            if x not in sol:
                sol.append(x)
                backtrack()
                sol.pop()

    backtrack()
    return ans