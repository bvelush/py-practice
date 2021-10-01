# https://www.educative.io/m/merge-two-sorted-linked-lists
# Problem statement: Given two sorted linked lists, merge them so that the resulting linked list is also sorted.

from dataclasses import dataclass


@dataclass
class N:
    v: int  # payload value
    n: 'N'  # pointer to the next element in LL

    def __init__(self, v: int, n: 'N' = None):
        self.v = v
        self.n = n

    def toStr(self) -> str:
        curr = self
        ret_val = ''
        while curr:
            ret_val += str(curr.v) + ', '
            curr = curr.n
        return ret_val[0:-2]  # curring out last comma


def test_toStr():
    ll = N(1, N(22, N(333)))
    assert ll.toStr() == '1, 22, 333'


def merge_ll(l1: N, l2: N) -> N:
    curr_l1 = l1
    curr_l2 = l2
    pre_head = N(0)  # a placeholder to keep a head
    curr_ret = pre_head
    while curr_l1 or curr_l2:
        if not curr_l1:
            consume_from = 2
        elif not curr_l2:
            consume_from = 1
        else:
            if curr_l1.v < curr_l2.v:
                consume_from = 1
            else:
                consume_from = 2

        if consume_from == 1:
            curr_ret.n = N(curr_l1.v)
            curr_l1 = curr_l1.n
        else:
            curr_ret.n = N(curr_l2.v)
            curr_l2 = curr_l2.n

        curr_ret = curr_ret.n

    return pre_head.n


def test_merge_ll():
    l1 = N(1, N(5, N(10)))
    assert l1.toStr() == '1, 5, 10'
    l2 = N(1, N(1, N(2, N(2, N(3, N(4, N(10)))))))
    assert l2.toStr() == '1, 1, 2, 2, 3, 4, 10'

    assert merge_ll(l1, l2).toStr() == '1, 1, 1, 2, 2, 3, 4, 5, 10, 10'
    assert merge_ll(l2, l1).toStr() == '1, 1, 1, 2, 2, 3, 4, 5, 10, 10'

    assert merge_ll(None, None) == None
    assert merge_ll(None, l1).toStr() == '1, 5, 10'
    assert merge_ll(l2, None).toStr() == '1, 1, 2, 2, 3, 4, 10'
