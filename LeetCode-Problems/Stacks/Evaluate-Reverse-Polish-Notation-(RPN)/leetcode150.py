from math import ceil, floor
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stk = []
        for t in tokens:
            if t in "+-*/":
                b, a = stk.pop(), stk.pop()

                if t == "+":
                    stk.append(a + b)
                elif t == "-":
                    stk.append(a - b)
                elif t == "*":
                    stk.append(a * b)
                else:
                    division = a / b
                    if division < 0:
                        stk.append(ceil(division))
                    else:
                        stk.append(floor(division))
            else:
                stk.append(int(t))

        return stk[0]


#Source : https://github.com/gahogg/Leetcode-Solutions/blob/main/Evaluate%20Reverse%20Polish%20Notation%20(RPN)%20-%20Leetcode%20150/Evaluate%20Reverse%20Polish%20Notation%20(RPN)%20-%20Leetcode%20150.py