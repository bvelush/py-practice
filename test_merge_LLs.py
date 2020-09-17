# https://www.codinginterview.com/facebook-interview-questions, #4
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


def merge_ll(a: N, b: N) -> N:
    curr_a = a
    curr_b = b
    pre_head = N(0)  # a placeholder to keep a head
    curr_ret = pre_head
    while curr_a or curr_b:
        pass
    return None
