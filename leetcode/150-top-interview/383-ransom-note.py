# https://leetcode.com/problems/ransom-note/description/?envType=study-plan-v2&envId=top-interview-150


from typing import List

# my solution
class Solution1:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_hash = self.build_hash(magazine)
        for ch in ransomNote:
            if ch not in mag_hash:
                return False
            mag_hash[ch] -= 1
            if mag_hash[ch] < 0:
                return False
        return True

    def build_hash(self, s: str) -> dict:
        ret_val = dict()
        for ch in s:
            if ch in ret_val.keys():
                ret_val[ch] += 1
            else: 
                ret_val[ch] = 1
        return ret_val

from collections import Counter
class Solution2:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomCounter = Counter(ransomNote)
        magCounter = Counter(magazine)
        return ransomCounter & magCounter == ransomCounter
            


    
test_cases = [
    {
        "ransomNote": "a", 
        "magazine": "b",
        "expected": False
    },
    {
        "ransomNote": "aa", 
        "magazine": "ab",
        "expected": False
    },
    {
        "ransomNote": "aa", 
        "magazine": "aab",
        "expected": True
    },
]

for case in range(len(test_cases)):
    ransomNote = test_cases[case]['ransomNote']
    magazine = test_cases[case]['magazine']
    print(f'=== Test case {case+1}. Input: {str}')
    expected = test_cases[case]['expected']
    s = Solution2()
    result = s.canConstruct(ransomNote, magazine)

    if expected != result:
        print(f'*** Test case {case+1} failed: expected {expected}, actual: {result}')
    else:
        print(f'Test case {case + 1} passed.  result: {result}')
