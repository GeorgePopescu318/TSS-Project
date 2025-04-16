class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stk = []

        for op in operations:
            if op == "+":
                stk.append(stk[-1] + stk[-2])
            elif op == "D":
                stk.append(stk[-1] * 2)
            elif op == "C":
                stk.pop()
            else:
                stk.append(int(op))

        return sum(stk)


#Source : https://github.com/gahogg/Leetcode-Solutions/blob/main/Baseball%20Game%20-%20Leetcode%20682/Baseball%20Game%20-%20Leetcode%20682.py