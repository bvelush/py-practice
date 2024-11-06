# https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150
# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
# The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, 
# you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are 
# not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.

from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)

        curr = 0
        while curr < k:
            if nums[curr] == val:
                k -= 1
                nums[curr] = nums[k]
            else: 
                curr += 1

        return k
        

test_cases = [
    {
        "nums": [3,2,2,3],
        "val": 3,
        "expectedResult": 2,
        "expectedNums": [2, 2]
    }, 
    {
        "nums": [0,1,2,2,3,0,4,2],
        "val": 2,
        "expectedResult": 5,
        "expectedNums": [0,0,1,3,4]
    }
]


for case in range(len(test_cases)):
    nums: List[int] = test_cases[case]['nums']
    val = test_cases[case]['val']
    expectedNums = test_cases[case]['expectedNums']
    expectedResult = test_cases[case]['expectedResult']
    s = Solution()
    result = s.removeElement(nums, val)

    if expectedResult != result:
        print(f'test case {case+1} failed: expected {expectedResult}, actual: {result}')
        break

    actual_result = nums[:result]
    actual_result.sort()
    if expectedNums != actual_result:
        print(f'test case {case+1} failed: expected {expectedNums}, actual: {actual_result}')
