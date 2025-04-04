# https://github.com/gahogg/Leetcode-Solutions/blob/main/Implement%20Trie%20(Prefix%20Tree)%20-%20Leetcode%20208/Implement%20Trie%20(Prefix%20Tree)%20-%20Leetcode%20208.py

class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        d = self.trie

        for c in word:
            if c not in d:
                d[c] = {}
            d = d[c]

        d['.'] = '.'

    def search(self, word: str) -> bool:
        d = self.trie

        for c in word:
            if c not in d:
                return False
            d = d[c]

        return '.' in d

    def startsWith(self, prefix: str) -> bool:
        d = self.trie

        for c in prefix:
            if c not in d:
                return False
            d = d[c]

        return True
        
        # Time: O(N) where N is the length of any string
        # Space: O(T) where T is the total number of stored characters