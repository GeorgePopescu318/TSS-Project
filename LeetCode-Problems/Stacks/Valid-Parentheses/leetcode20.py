class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {")": "(", "}": "{", "]": "["}
        stk = []

        for c in s:
            if c not in hashmap:
                stk.append(c)
            else:
                if not stk:
                    return False
                else:
                    popped = stk.pop()
                    if popped != hashmap[c]:
                        return False

        return not stk


#Source : https://github.com/gahogg/Leetcode-Solutions/blob/main/Valid%20Parentheses%20-%20Leetcode%2020/Valid%20Parentheses%20-%20Leetcode%2020.py