# https://leetcode.com/problems/longest-common-prefix/description/?envType=study-plan-v2&envId=top-interview-150


from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ret_val = ""
        for slice in zip(*strs):
            ch = slice[0]
            # testing for all elements of slice to be the same
            if len(set(slice)) != 1:
                return ret_val
            # less effective way:
            # for i in range(1, len(slice)):
            #     if ch != slice[i]:
            #         return ret_val
            ret_val += ch
        return ret_val

    
test_cases = [
    {
        "strs": ["flower","flow","flight"],
        "expected": "fl"
    },
    {
        "strs": ["dog","racecar","car"],
        "expected": ""
    }
]

for case in range(len(test_cases)):
    strs = test_cases[case]['strs']
    print(f'=== Test case {case+1}. Input: {str}')
    expected = test_cases[case]['expected']
    s = Solution()
    result = s.longestCommonPrefix(strs)

    if expected != result:
        print(f'*** Test case {case+1} failed: expected {expected}, actual: {result}')
    else:
        print(f'Test case {case + 1} passed.  result: {result}')
