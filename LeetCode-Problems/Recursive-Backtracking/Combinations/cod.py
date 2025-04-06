def combine(n: int, k: int) -> list[list[int]]:
    ans, sol = [], []

    def backtrack(x):
        if len(sol) == k:
            ans.append(sol[:])
            return

        left = x
        still_need = k - len(sol)

        if left > still_need:
            backtrack(x - 1)

        sol.append(x)
        backtrack(x - 1)
        sol.pop()

    backtrack(n)
    return ans