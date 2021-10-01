from typing import List


def magic_triplet(a: List[int]) -> None:
    '''
    Finds all triplets that sum up to 0 (like [3, -7, 4] or [0, 0, 0])
    Simple solution (expected to be solved in 20 mins)
    '''
    arr_len = len(a)
    if arr_len < 3:
        raise Exception(
            'it is expected that input array has at least 3 elements')

    for i in range(0, arr_len-2):
        for j in range(i+1, arr_len - 1):
            pre_sum = a[i] + a[j]
            for k in range(j+1, arr_len):
                if pre_sum + a[k] == 0:
                    print(i, j, k, a[i], a[j], a[k])


arr = [2, -3, 0, -7, 5, 1, 7, 18, -5]

magic_triplet(arr)

# Next question on the interview after solving this, is how to test this code?
# Expected answer something like write for a case for empty array, for array with exactly 3 elements, etc.
#
