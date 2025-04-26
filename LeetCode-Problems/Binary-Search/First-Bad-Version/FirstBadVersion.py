#https://github.com/gahogg/Leetcode-Solutions/blob/main/First%20Bad%20Version%20-%20Leetcode%20278/First%20Bad%20Version%20-%20Leetcode%20278.py

def isBadVersion(version: int) -> bool:
    return version >= 4

def firstBadVersion(self, n: int) -> int:
        for version in range(1, n + 1):
            if isBadVersion(version):
                return version