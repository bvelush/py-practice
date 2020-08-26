# move all zeros to the beginning keeping the order
# Given an integer array, move all elements that are equal to 0 to the left
# while maintaining the order of other elements in the array.
# https://www.codinginterview.com/facebook-interview-questions, #1

import functools


def zeros_in_array(a: [int]) -> [int]:
    ret_val = [0] * len(a)
    ret_zeros = 0
    ret_others = len(a) - 1

    for i in range(len(a) - 1, -1, -1):
        if a[i] == 0:
            ret_zeros += 1
        else:
            ret_val[ret_others] = a[i]
            ret_others -= 1

    return ret_val


def compare_lists(a, b: [int]) -> bool:
    return functools.reduce(
        lambda r1, r2:
        r1 and r2,
        map(lambda m1, m2: m1 == m2, a, b),
        True)


def test_input():
    assert zeros_in_array([]) == []
    assert compare_lists(zeros_in_array([0, 0, 0]), [0, 0, 0])
    assert compare_lists(zeros_in_array([1, 2, 3]), [1, 2, 3])
    assert compare_lists(zeros_in_array([1, 0, 3]), [0, 1, 3])
    assert compare_lists(zeros_in_array(
        [0, 0, 1, 0, 2, 3, 0, 4, 0, 0, 5, 6, 0]),
        [0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6])
    assert compare_lists(zeros_in_array(
        [1, 10, 20, 0, 59, 63, 0, 88, 0]),
        [0, 0, 0, 1, 10, 20, 59, 63, 88])
