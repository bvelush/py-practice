# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/?envType=study-plan-v2&envId=top-interview-150


from typing import List

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l = len(needle)
        for i in range(len(haystack)-l+1):
            if haystack[i:i+l] == needle:
                return i
        return -1

    
test_cases = [
    {
        "hay": "sadbutsad",
        "needle": "sad",
        "expected": 0
    },
        {
        "hay": "sabutsad",
        "needle": "sad",
        "expected": 5
    },
    {
        "hay": "eeesadbutsad",
        "needle": "sad",
        "expected": 3
    },
    {
        "hay": "sadbutsad",
        "needle": "sk",
        "expected": -1
    }
]


for case in range(len(test_cases)):
    hay = test_cases[case]['hay']
    needle = test_cases[case]['needle']
    print(f'=== Test case {case+1}. Input: {hay}, {needle}')
    expected = test_cases[case]['expected']
    s = Solution()
    result = s.strStr(hay, needle)

    if expected != result:
        print(f'*** Test case {case+1} failed: expected {expected}, actual: {result}')
    else:
        print(f'Test case {case + 1} passed.  result: {result}')
