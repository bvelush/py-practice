# https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for ch in s:
            if i < len(s)-1:
                pass
            else:
                pass
        return True


if __name__ == "__main__":
    test_cases = [
        {
            "str": "abc", 
            "t": "ahbgdc",
            "expected": True
        },
        {
            "str": "axc", 
            "t": "ahbgdc",
            "expected": False
        },        
        {
            "str": "axc", 
            "t": "ahbgdceexd",
            "expected": False
        },
    ]

    for case in range(len(test_cases)):
        str = test_cases[case]['str']
        t = test_cases[case]['t']
        print(f'=== Test case {case+1}. Input: {str}')
        expected = test_cases[case]['expected']
        s = Solution()
        result = s.isSubsequence(str, t)

        if expected != result:
            print(f'*** Test case {case+1} failed: expected {expected}, actual: {result}')
        else:
            print(f'Test case {case + 1} passed.  result: {result}')
