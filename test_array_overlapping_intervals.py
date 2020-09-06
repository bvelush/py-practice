# Merge overlapping intervals
# Given a list of intervals, merge all the overlapping intervals
# to produce a list that has only mutually exclusive intervals.
# https://www.codinginterview.com/facebook-interview-questions, #2


import functools
from dataclasses import dataclass


@dataclass
class I:
    l: int
    r: int


def intervals(intervals: [I]) -> [I]:
    if intervals == []:
        return []

    sorted_intervals = sorted(intervals, key=lambda i: i.l)

    ret_val = [sorted_intervals[0]]
    curr = 0
    for i in range(1, len(sorted_intervals)):
        incoming = sorted_intervals[i]
        if incoming.l <= ret_val[curr].r:
            if incoming.r > ret_val[curr].r:
                ret_val[curr].r = incoming.r
        else:
            ret_val.append(incoming)
            curr += 1
    return ret_val


def compare_lists(l1, l2):
    if (l1 == [] and l2 != []) or (l2 == [] and l1 != []):
        return False
    return functools.reduce(lambda r1, r2: r1 and r2, map(lambda m1, m2: m1 == m2, l1, l2), True)


def test_compare_lists():
    assert compare_lists([], []) == True
    assert compare_lists([], [1]) == False
    assert compare_lists([1], []) == False
    assert compare_lists([1], [2]) == False
    assert compare_lists([I(1, 2)], [I(1, 2)])  # testing with complex objects


def test_intervals():
    assert compare_lists(
        intervals([I(-1, 2), I(2, 3), I(7, 10), I(6, 7), I(5, 8)]),
        [I(-1, 3), I(5, 10)])
    assert compare_lists(
        intervals([I(7, 9), I(3, 8), I(-1, 1), I(4, 6), I(1, 2)]),
        [I(-1, 2), I(3, 9)])
    assert compare_lists(
        intervals([I(1, 5), I(3, 7), I(4, 6), I(6, 8)]),
        [I(1, 8)])
    assert compare_lists(
        intervals([I(10, 12), I(12, 15)]),
        [I(10, 15)])
