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

# this works 5% faster than others, 84% memory
class Solution2:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = len(nums)
        i = 1
        while i < k:
            if nums[i] != nums[i-1]:
                i += 1          # skip to next if elements are different
            else:
                del_begin = i   # curr element is duplicate
                del_end = i
                while del_end < k and nums[del_end] == nums[del_begin]: # iterate to the end of array or till end of duplicate series
                    del_end += 1
                if del_end < k:
                    # moving elements left to offset places
                    offset = del_end - del_begin
                    for j in range(del_end, k):
                        nums[j-offset] = nums[j]
                    k -= offset
                else:
                    return del_begin
        return k

class Solution3:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j
    
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
    print(f'=== Test case {case+1}. Input: {nums}')
    expectedNums = test_cases[case]['expectedNums']
    expectedResult = test_cases[case]['expectedResult']
    s = Solution3()
    result = s.removeDuplicates(nums)

    actual_result = nums[:result]
    actual_result.sort()
    if expectedNums != actual_result:
        print(f'*** Test case {case+1} failed: expected {expectedNums}, actual: {actual_result}')
    else:
        print(f'Test case {case + 1} passed.  result: {actual_result}, {result}')
