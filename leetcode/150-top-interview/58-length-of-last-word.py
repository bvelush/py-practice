# https://leetcode.com/problems/length-of-last-word/description/?envType=study-plan-v2&envId=top-interview-150


from typing import List

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        curr = len(s)-1
        while s[curr] == ' ':
            curr -= 1

        word_end = curr
        while curr > -1 and s[curr] != ' ':
            curr -= 1
        
        return word_end - curr


    
test_cases = [
    {
        "str": "Hello World",
        "expected": 5
    },
    {
        "str": "World",
        "expected": 5
    },
    {
        "str": "World  ",
        "expected": 5
    },
    {
        "str": "  World",
        "expected": 5
    },
    {
        "str": " World ",
        "expected": 5
    },
    {
        "str": "   fly me   to   the moon  ",
        "expected": 4
    },
    {
        "str": "luffy is still joyboy",
        "expected": 6
    },
    
]

for case in range(len(test_cases)):
    str = test_cases[case]['str']
    print(f'=== Test case {case+1}. Input: {str}')
    expected = test_cases[case]['expected']
    s = Solution()
    result = s.lengthOfLastWord(str)

    if expected != result:
        print(f'*** Test case {case+1} failed: expected {expected}, actual: {result}')
    else:
        print(f'Test case {case + 1} passed.  result: {result}')
