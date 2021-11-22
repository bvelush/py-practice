# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid(marked 'Finish' in the diagram below).
# How many possible unique paths are there?

# Example 1:
# Input: m = 3, n = 7
# Output: 28

# Example 2:
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down

# Example 3:
# Input: m = 7, n = 3
# Output: 28

# Example 4:
# Input: m = 3, n = 3
# Output: 6

# result on LeetCode:
# Runtime: 36 ms, faster than 25.91 % of Python3 online submissions for Unique Paths.
# Memory Usage: 14.8 MB, less than 5.22 % of Python3 online submissions for Unique Paths.
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cashe = {(1, 1): 1}

        def _uniquePaths(m: int, n: int) -> int:
            if (m, n) in cashe or (n, m) in cashe:
                return cashe[(m, n)]
            mm = 0
            nn = 0
            if m != 0:
                mm = _uniquePaths(m-1, n)
            if n != 0:
                nn = _uniquePaths(m, n-1)
            ret_val = mm + nn
            cashe[(m, n)] = cashe[(n, m)] = ret_val
            return ret_val

        return _uniquePaths(m, n)


class Solution1:
    def uniquePaths(self, m: int, n: int) -> int:
        # do not use [[0]*n]*m, because it creates references of the single variable
        solutions = [[0 for _ in range(n)] for _ in range(m)]
        for nn in range(-1, -n-1, -1):
            solutions[-1][nn] = 1
        for mm in range(-2, -m-1, -1):
            for nn in range(-1, -n-1, -1):
                if nn == -1:
                    solutions[mm][nn] = 1
                else:
                    solutions[mm][nn] = solutions[mm][nn+1] + \
                        solutions[mm+1][nn]
        return solutions[0][0]


def test_uniquePaths1():
    s = Solution()
    print(s.uniquePaths(1, 1))  # 1
    print(s.uniquePaths(2, 1))  # 1
    print(s.uniquePaths(1, 5))  # 1
    print(s.uniquePaths(5, 1))  # 1
    print(s.uniquePaths(7, 3))  # 28
    print(s.uniquePaths(23, 12))  # 193536720


def test_uniquePaths2():
    s = Solution1()
    # print(s.uniquePaths(1, 1))
    print(s.uniquePaths(2, 1))  # 1
    # print(s.uniquePaths(1, 5))
    # print(s.uniquePaths(5, 1))
    # print(s.uniquePaths(7, 3))
    # print(s.uniquePaths(23, 12))


test_uniquePaths1()
test_uniquePaths2()
