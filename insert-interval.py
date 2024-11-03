# https://leetcode.com/problems/insert-interval/?envType=list&envId=du693s

from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        low_interval_index = -1
        for i in range(len(intervals)):
            if intervals[i][1] >= newInterval[0]:
                low_interval_index = i
                break

        if low_interval_index >= 0:
            high_interval_index = -1
            for i in range(len(intervals)-1, -1, -1):
                if intervals[i][0] <= newInterval[0]:
                    high_interval_index = i
                    break

        return intervals

        



S = Solution()
intervals = [[1,3],[6,9]]
newInterval = [2,5]
output = [[1,5],[6,9]]
assert(S.insert(intervals, newInterval) == output)

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
output = [[1,2],[3,10],[12,16]]
assert(S.insert(intervals, newInterval) == output)
