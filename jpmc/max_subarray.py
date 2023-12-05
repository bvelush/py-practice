# Given an array of integers, find the subarray which has the largest sum
import math
from typing import List

def max_subarray(nums: List[int]) -> [int, int, int]: # returning the first and last-1 positions of the subarray
    # l = 0
    # r = 0
    sum_ = 0
    max_sum = -math.inf
    l_bound = 0
    r_bound = 0
    for r in range(len(nums)):
        sum_ += nums[r]
        if max_sum < sum_:
            max_sum = sum_
            r_bound = r+1
    
    sum_ = max_sum
    if (r_bound > 1):
        for l in range(r_bound):
            sum_ -= nums[l]
            if max_sum < sum_:
                max_sum = sum_
                l_bound = l+1

    return l_bound, r_bound, max_sum # sum(nums[l_bound:r_bound])

def test(arr: List[int]):
    answer = max_subarray(arr)
    ans_list = arr[answer[0]:answer[1]]
    print(ans_list)
    print(sum(ans_list))
    print(f'--- {answer[2]} ----\n')

test([1, 2, 3, -5, 0, 1, 2])
test([-2,1,-3,4,-1,2,1,-5,4])
test([1])
test([5,4,-1,7,8])
test([-1])
test([-2, -1]) 

