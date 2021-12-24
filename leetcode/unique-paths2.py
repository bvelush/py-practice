
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        solutions = [[0 for _ in range(n)] for _ in range(m)]

        fill_with = 1
        for nn in range(-1, -n-1, -1):

            if (fill_with == 1) and (obstacleGrid[-1][nn] == 1):
                fill_with = 0
            solutions[-1][nn] = fill_with

        fill_with = 1
        for mm in range(-1, -m-1, -1):
            if (fill_with == 1) and (obstacleGrid[mm][-1] == 1):
                fill_with = 0
            solutions[mm][-1] = fill_with

        for mm in range(-2, -m-1, -1):
            for nn in range(-2, -n-1, -1):
                if obstacleGrid[mm][nn] == 1:
                    solutions[mm][nn] = 0
                else:
                    solutions[mm][nn] = solutions[mm][nn+1] + \
                        solutions[mm+1][nn]

        return solutions[-m][-n]


class Solution_recursive:
    solutions = dict()

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        pass

    def _uniquePaths(self, m: int, n: int, obstacleGrid: List[List[int]]) -> int:
        pass


test_cases = [
    [
        [
            [0, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 0]
        ],
        4
    ],
    [
        [
            [0, 0],
            [0, 1]
        ],
        0
    ]
]


def test(test_cases):
    for test, answer in test_cases:
        assert(Solution().uniquePathsWithObstacles(test) == answer)


test(test_cases)
