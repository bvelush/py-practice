# https://leetcode.com/problems/valid-palindrome/description/?envType=study-plan-v2&envId=top-interview-150

# this is a basic solution, works great, beats 55%
import re
pattern = re.compile('[\W_]+')

class Solution_slower:
    def isPalindrome(self, s: str) -> bool:
        s = pattern.sub('', s.lower())
        l = 0
        r = len(s)-1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

# but there is a better way: if the character is not isalnum, just skip it. Interestingly, the time is THE SAME
class Solution2:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        while l < r:
            sl = s[l]
            sr = s[r]
            if not sl.isalnum():
                l += 1
                continue
            if not sr.isalnum():
                r -= 1
                continue
            if sl.lower() != sr.lower():
                return False
            l += 1
            r -= 1
        return True

# using list comprehensions and symmetric addressing (~)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [ch.lower() for ch in s if ch.isalnum()]
        ret_val = all(s[i] == s[~i] for i in range(len(s)//2))
        return ret_val


if __name__ == "__main__":
    test_cases = [
        {
            "str": "A man, a plan, a canal: Panama", 
            "expected": True
        },
        {
            "str": "race a car", 
            "expected": False
        },    
        {
            "str": "", 
            "expected": True
        },
    ]

    for case in range(len(test_cases)):
        str = test_cases[case]['str']
        print(f'=== Test case {case+1}. Input: {str}')
        expected = test_cases[case]['expected']
        s = Solution()
        result = s.isPalindrome(str)

        if expected != result:
            print(f'*** Test case {case+1} failed: expected {expected}, actual: {result}')
        else:
            print(f'Test case {case + 1} passed.  result: {result}')
