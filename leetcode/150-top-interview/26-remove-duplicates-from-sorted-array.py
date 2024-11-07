# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
# Given an integer array nums sorted in non-decreasing order, remove the duplicates 
# in-place such that each unique element appears only once. The relative order of the 
# elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements 
# in the order they were present in nums initially. The remaining elements of nums are not 
# important as well as the size of nums.
# Return k.

from typing import List

# solution 1: Naive. Works, but too long, doesn't pass the time complexity
class Solution1:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = len(nums)
        if k < 2:
             return k
        
        curr = 1
        while curr < k:
            if nums[curr] == nums[curr-1]:
                for i in range(curr, k-1):
                    nums[i] = nums[i+1] 
                k -= 1
            else:
                curr += 1

        return k
        

class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = len(nums)
        if k < 2:
             return k
        
        i = 0
        j = 1
        while i < k-1:
            if nums[i] != nums[j]:
                i += 1
                j += 1
            else:
                

        return k


test_cases = [
    {
        "nums": [1,1],
        "expectedResult": 1,
        "expectedNums": [1]
    }, 
    {
        "nums": [1,1,2],
        "expectedResult": 2,
        "expectedNums": [1, 2]
    }, 
    {
        "nums": [0,0,1,1,1,2,2,3,3,4],
        "expectedResult": 5,
        "expectedNums": [0,1,2,3,4]
    }
]


for case in range(len(test_cases)):
    nums: List[int] = test_cases[case]['nums']
    expectedNums = test_cases[case]['expectedNums']
    expectedResult = test_cases[case]['expectedResult']
    s = Solution2()
    result = s.removeDuplicates(nums)

    actual_result = nums[:result]
    actual_result.sort()
    if expectedNums != actual_result:
        print(f'test case {case+1} failed: expected {expectedNums}, actual: {actual_result}')
