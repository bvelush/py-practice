# https://leetcode.com/problems/h-index/description/?envType=study-plan-v2&envId=top-interview-150

from typing import List

# beats 100/16
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations) == 0:
            return 0
        
        citations.sort(reverse=True)
        max_h = min(1, citations[0])
        for i in range(1, len(citations)):
            curr_h = min(i+1, citations[i])
            if max_h < curr_h:
                max_h = curr_h
            else: 
                return max_h
        return max_h
    
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
