# https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=top-interview-150

# beats 100%, memory beats 14%
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for ch in s:
            ch_found = False
            while i < len(t) and not ch_found:
                if t[i] == ch:
                    ch_found = True
                i += 1
            if not ch_found:
                return False
        
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
        {
            "str": "aaaaaa", 
            "t": "bbaaaa",
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
