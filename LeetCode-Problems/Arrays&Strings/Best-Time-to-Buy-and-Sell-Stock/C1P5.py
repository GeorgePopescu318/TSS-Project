### GitHub
### https://github.com/gahogg/Leetcode-Solutions/blob/main/Best%20Time%20to%20Buy%20and%20Sell%20Stock%20-%20Leetcode%20121/Best%20Time%20to%20Buy%20and%20Sell%20Stock%20-%20Leetcode%20121.py
###
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time: O(n)
        # Space: O(1)
        min_price = float('inf')
        max_profit = 0        
        
        for price in prices:
            profit = price - min_price
            
            min_price = min(price, min_price)
            max_profit = max(profit, max_profit)
                
        return max_profit