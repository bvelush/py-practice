# Merge overlapping intervals
# Given a list of intervals, merge all the overlapping intervals
# to produce a list that has only mutually exclusive intervals.
# https://www.educative.io/m/merge-overlapping-intervals


import functools
from dataclasses import dataclass


@dataclass
class I:
    l: int
    r: int


# the problem statement is vague. I was assuming that incoming data are not sorted.
# the solution idea is that I am sorting incoming data based on a lower boundary first,
# then creating output with the first interval and then
# taking one-by-one sorted incoming intervals to either do nothing (if they fully fit into
# one of the output intervals), or increase a higher boundary, or create new interval if
# they don't overlap. Lower boundary can't be increased because of the sorting: each next incoming
# interval is guaranteed to have lower boundary greater or equal to those in output.
# Note that the reference solution DOES NOT work properly on unsorted intervals, and it is much more
# complex than my solution
def intervals(intervals: [I]) -> [I]:
    if intervals == []:
        return []

    sorted_intervals = sorted(intervals, key=lambda i: i.l)

    # the first interval from input -> to output
    ret_val = [sorted_intervals[0]]
    curr = 0
    for i in range(1, len(sorted_intervals)):  # for the rest in input...
        incoming = sorted_intervals[i]
        # case of overlapping lower boundary of the input interval
        if incoming.l <= ret_val[curr].r:
            if incoming.r > ret_val[curr].r:  # is the high boundary larger?
                # increase higher boundary of output interval
                ret_val[curr].r = incoming.r
        else:  # case of the current output interval is not overlapping with incoming
            ret_val.append(incoming)  # add it to the output
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
