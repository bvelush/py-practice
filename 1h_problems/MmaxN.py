import math
import random
import time
from typing import List

'''
This little project is an attempt to find out which is the fastest way to do a simple thing:
    Find M top numbers in the array of N. For example, find 3 maximum numbers in array
    [2, -1, 4, 0, 3, -5, 0, 4] => answer is [4, 4, 3]

    3 different ways to solve the problem:

        1. Naive: for each array element insert it (if possible) to the results array.
        2. Sort, than take tail M elements
        3. Reverse sort, than take head M elements

    *Conclusions:* even on M=5 any sort is better. There is no difference between sort algorythms, so #3 wins as
    it looks cleanest.

    Results for M=5:

    10000000
    generate_array()): 36.42202067375183 s
    maxm()): 11.41899299621582 s
    [99999943, 99999939, 99999930, 99999927, 99999910]
    maxm_with_sort()): 4.840341567993164 s
    [99999943, 99999939, 99999930, 99999927, 99999910]
    maxm_with_sort_reversed()): 4.8144261837005615 s
    [99999943, 99999939, 99999930, 99999927, 99999910]
    == ===

    100000000
    generate_array()): 378.8789300918579 s
    maxm()): 116.5107889175415 s
    [99999999, 99999999, 99999994, 99999994, 99999994]
    maxm_with_sort()): 71.34384655952454 s
    [99999999, 99999999, 99999994, 99999994, 99999994]
    maxm_with_sort_reversed()): 71.68428540229797 s
    [99999999, 99999999, 99999994, 99999994, 99999994]

    Worst part is that naive version execution time grows exponentualy with growth of M,
    while #2, 3 stay completely the same (since it is just a head/tail iterator of the
    sorted array)

'''


def timerfunc(func):
    """
    A timer decorator
    """
    def function_timer(*args, **kwargs):
        """
        A nested function for timing other functions
        """
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()
        runtime = end - start
        msg = "{func}()) : {time} s"
        print(msg.format(func=func.__name__,
                         time=runtime))
        return value
    return function_timer


@ timerfunc
def generate_array(n: int, min: int = 0, max: int = 100) -> List[int]:
    return [random.randint(min, max) for _ in range(n)]


@ timerfunc
def maxm(arr: List[int], m: int) -> List[int]:
    def array_insert(arr: List[int], index: int, value: int) -> None:
        '''
        inserts value to an array at the index, moving rest of elements
        to the right. Last element of the array is lost
        '''
        for i in range(len(arr) - 1, index, -1):
            arr[i] = arr[i-1]
        arr[index] = value

    res = [-math.inf for _ in range(m)]
    for item in arr:
        for res_i in range(m):
            if item > res[res_i]:
                array_insert(res, res_i, item)
                break
    return res


@ timerfunc
def maxm_with_sort(arr: List[int], m: int) -> List[int]:
    '''
    Sorts ascending, then returns M elements from the end
    '''
    return sorted(arr)[-1:-m-1:-1]


@ timerfunc
def maxm_with_sort_reversed(arr: List[int], m: int) -> List[int]:
    '''
    Sorts descenging, then returns M elements from the beginning
    '''
    return sorted(arr, reverse=True)[:m]  # I feek this is cleanest way


min_n_power = 3
max_n_power = 6
main_array = generate_array(10 ** max_n_power, -10 ** 10, 10 ** 10)
arrays = [list(main_array[:10**length])
          for length in range(min_n_power, max_n_power+1)]

for array in arrays:
    for m in range(10, 900, 100):
        n = len(array)
        print(f'N={n}, M={m}')
        res1 = maxm(array, m)
        res2 = maxm_with_sort(array, m)
        res3 = maxm_with_sort_reversed(array, m)
        if (res1 != res2 or res1 != res3):
            raise Exception(
                f'something is wrong, results are different: \nres1={res1}, \nres2={res2}, \nres3={res3}')
        print('=====\n')
