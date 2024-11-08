# https://leetcode.com/problems/roman-to-integer/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def romanToInt(self, s: str) -> int:
        ret_val = 0
        vals = {
            'I': 1, 
            'V': 5, 
            'X': 10, 
            'L': 50, 
            'C': 100, 
            'D': 500, 
            'M': 1000
        }
        for i in range(1, len(s)):
            curr = vals[s[i-1]]
            next = vals[s[i]]

            if curr < next:
                ret_val -= curr
            else:
                ret_val += curr
        ret_val += vals[s[-1]]
        return ret_val

test_cases = [
    {
        "s": "III",
        "expected": 3
    }, 
        {
        "s": "LVIII",
        "expected": 58
    }, 
        {
        "s": "MCMXCIV",
        "expected": 1994
    }
]

for case in range(len(test_cases)):
    str = test_cases[case]['s']
    expected = test_cases[case]['expected']
    s = Solution()
    result = s.romanToInt(str)

    if expected != result:
        print(f'test case {case+1} failed: Input: {str}, expected {expected}, actual: {result}')
        break
