# https://leetcode.com/problems/insert-interval/?envType=list&envId=du693s
not solved yet
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        pass

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            for j in range(len(res)):
                if 
    

S = Solution()
intervals = [[1,3],[6,9]]
newInterval = [2,5]
output = [[1,5],[6,9]]
assert(S.insert(intervals, newInterval) == output)

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
output = [[1,2],[3,10],[12,16]]
assert(S.insert(intervals, newInterval) == output)
