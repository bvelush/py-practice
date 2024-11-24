# https://leetcode.com/problems/h-index/description/?envType=study-plan-v2&envId=top-interview-150

from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:

        return 0

    
test_cases = [
    {
        "citations": [3,0,6,1,5], 
        "expected": 3
    }, 
    {
        "citations": [1,3,1],
        "expected": 1
    }, 
    {
        "citations": [0, 1],
        "expected": 1
    },
    {
        "citations": [0],
        "expected": 0
    },
    {
        "citations": [11, 15],
        "expected": 2
    },
    {
        "citations": [0, 2],
        "expected": 1
    }
]

for case in range(len(test_cases)):
    citations = test_cases[case]['citations']
    print(f'=== Test case {case+1}. Input: {citations}')
    expected = test_cases[case]['expected']
    s = Solution()
    result = s.hIndex(citations)

    if expected != result:
        print(f'*** Test case {case+1} failed: expected {expected}, actual: {result}')
    else:
        print(f'Test case {case + 1} passed.  result: {result}')
