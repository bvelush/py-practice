# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=study-plan-v2&envId=top-interview-150

from typing import List
# naive solution, O(N*N). Doesn't pass the complexity test
class Solution_slow:
    def maxProfit(self, prices: List[int]) -> int:
        best_deal = 0
        for i in range(len(prices)-1):
            for j in range(i, len(prices)):
                curr = prices[i]
                future = prices[j]
                deal = future - curr
                if deal > best_deal:
                    best_deal = deal   
        return best_deal
    
# Kadane's algorythm (https://algodaily.com/lessons/kadanes-algorithm-explained/python)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit

        
test_cases = [
    {
        "prices": [7,1,5,3,6,4],
        "expected": 5
    },
    {
        "prices": [7,6,4,3,1],
        "expected": 0
    },
    
]

for case in range(len(test_cases)):
    prices = test_cases[case]['prices']
    print(f'=== Test case {case+1}. Input: {prices}')
    expected = test_cases[case]['expected']
    s = Solution()
    result = s.maxProfit(prices)

    if expected != result:
        print(f'*** Test case {case+1} failed: expected {expected}, actual: {result}')
    else:
        print(f'Test case {case + 1} passed.  result: {result}')