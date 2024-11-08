# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150
# Given an integer array nums sorted in non-decreasing order, remove some duplicates 
# in-place such that each unique element appears at most twice. The relative order 
# of the elements should be kept the same.

# Since it is impossible to change the length of the array in some languages, you 
# must instead have the result be placed in the first part of the array nums. More 
# formally, if there are k elements after removing the duplicates, then the first k 
# elements of nums should hold the final result. It does not matter what you leave 
# beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying the 
# input array in-place with O(1) extra memory.

from typing import List

# solution 1: Naive. Works, but too long, doesn't pass the time complexity
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

    
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
    }, 
    {
        "nums": [1,1,1,2,2,3],
        "expectedResult": 5,
        "expectedNums": [1, 1, 2, 2, 3]
    }, 
    {
        "nums": [0,0,1,1,1,1,2,3,3],
        "expectedResult": 7,
        "expectedNums": [0,0,1,1,2,3,3]
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
