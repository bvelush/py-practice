# *** REPEAT SOLUTION ONE MORE TIME ***

# https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside 
# the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements 
# denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. 
# nums2 has a length of n.



from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        
        r = m+n-1
        mi=m-1
        ni=n-1
        while ni >= 0:
            if mi >= 0 and nums1[mi] > nums2[ni]:
                nums1[r] = nums1[mi]
                mi -= 1
            else:
                nums1[r] = nums2[ni]
                ni -= 1
            
            r -= 1


test_cases = [
    {
        "nums1": [1,2,3,0,0,0],
        "m": 3,
        "nums2": [2, 5, 6],
        "n": 3,
        "expected": [1, 2, 2, 3, 5, 6]
    }, 
    {
        "nums1": [1],
        "m": 1,  
        "nums2": [], 
        "n": 0,  
        "expected": [1] 
    },
    {
        "nums1": [0],
        "m": 0,  
        "nums2": [1], 
        "n": 1,  
        "expected": [1] 
    }
]


for case in range(len(test_cases)):
    nums1 = test_cases[case]["nums1"]
    m = test_cases[case]["m"]
    nums2 = test_cases[case]["nums2"]
    n = test_cases[case]["n"]
    expected = test_cases[case]["expected"]
    s = Solution()
    s.merge(nums1, m, nums2, n)
    if nums1 != expected:
        print(f'test case {case+1} failed: expected {expected}, actual: {nums1}')
    else:
        print(f'test case {case+1} passed')
        