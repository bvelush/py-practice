# *** solve with O(N) and memory O(1)

# https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.

from typing import List

# simple solution, O(nlog(n)), Mem: O(1)
class Solution1:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
    

# O(N), O(1)
class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        res = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if count == 0:
                res = nums[i]
                count = 1
            else:
                if nums[i] == res:
                    count += 1
                else:
                    count -= 1
        return res


test_cases = [
    {
        "nums": [1, 2, 1],
        "expected": 1
    },
        {
        "nums": [1, 2, 3, 1, 2, 1, 1],
        "expected": 1
    },
    {
        "nums": [2, 2, 1],
        "expected": 2
    },
    {
        "nums": [1, 2, 1, 2, 2],
        "expected": 2
    },
    {
        "nums": [3, 2, 3],
        "expected": 3
    },
     {
        "nums": [2,2,1,1,1,2,2],
        "expected": 2
    }
]

for case in range(len(test_cases)):
    nums = test_cases[case]['nums']
    expected = test_cases[case]['expected']

    s = Solution2()
    result = s.majorityElement(nums)
    if result != expected:
        print(f'*** Test case {case+1} failed. Input: {nums} Expected: {expected}, result: {result}')
    else:
        print(f'Test case {case+1} passed: Input: {nums}, result: {result}')