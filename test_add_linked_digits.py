# Given the head pointers of two linked lists where each linked list represents an integer number (each node is a digit), add them and return the resulting linked list.
# https://www.educative.io/m/add-two-integers
# numbers are represented as linked lists of digits, head is the lowest: 29 => 9->2->null

from dataclasses import dataclass


@dataclass
class D:  # digit
    v: int  # value

    # next digit. D in quotes because of the recursive definitions (https://stackoverflow.com/questions/38340808/recursive-typing-in-python-3-5)
    n: 'D'

    def __init__(self, v: int, n: 'D' = None):
        self.v = v
        self.n = n

    def toInt(self) -> int:
        pow = 1
        curr = self
        ret_val = 0
        while curr:
            ret_val += curr.v * pow
            pow *= 10
            curr = curr.n
        return ret_val


# helper function to extract the current digit and progress to the next one
def digit(a: D) -> (int, D):
    if a:
        return (a.v, a.n)
    return (0, None)


# I wrote this entire function in 10 minutes, writing the test first.
# suprprisingly :), it worked immediately. The code is pretty self-explanatory:
# we are adding digit by digit. If the result of addition is >10, then setting the carry bit
# and adjusting the current digit result back to one digit (9+9 => 8 plus a carry bit)
# we process until we have any digits or carry bit left in any of numbers.
# why carry bit needs to be in the while? because 50+50 should run 3 times to get 100
# what's the magic with the ret_val? it's a common practice in linked list (LL) problems
# to hold the value of the future list head
# before returning the result, we stripe out this heading element, returning the real head of the LL

# after looking at the reference implementation at https://www.educative.io/m/add-two-integers,
# I find out that my implementation is easier to read and is more compact. Also, the problem statement
# didn't say how to return the result, so I assumed it's the same LL format as original numbers
# (otherwise what's the point?!), but looks they are returning a plain INT with more code. Lame.
def add(a: D, b: D) -> D:

    curr_a = a
    curr_b = b
    carry = 0
    pre_head = D(-1)  # -1 is a placeholder value
    curr_res = pre_head

    while curr_a or curr_b or carry:
        curr_a_digit, curr_a = digit(curr_a)
        curr_b_digit, curr_b = digit(curr_b)
        curr_res_digit = curr_a_digit + curr_b_digit + carry

        if curr_res_digit > 9:
            curr_res_digit -= 10
            carry = 1
        else:
            carry = 0

        curr_res.n = D(curr_res_digit)
        curr_res = curr_res.n

    return pre_head.n  # striping out the placeholder


def test_D():
    d = D(5)
    assert d.toInt() == 5
    d = D(3, D(2, D(1)))  # 123
    assert d.toInt() == 123


def test_digit():
    a = D(2, D(4))  # 42
    resInt, resDigit = digit(a)
    assert resInt == 2
    assert resDigit == a.n
    resInt, resDigit = digit(resDigit)
    assert resInt == 4
    assert resDigit == None
    resInt, resDigit = digit(resDigit)
    assert resInt == 0
    assert resDigit == None


def test_addition():
    assert add(D(1), D(2)).toInt() == 3  # 1+2 == 3
    assert add(D(1, D(1)), D(2, D(2))).toInt() == 33  # 11 + 22 == 33
    # testing simple carry
    a = D(9, D(2))  # a = 29
    b = D(3, D(9))  # b = 93
    assert add(a, b).toInt() == 122  # 29 + 93 == 122
    # testing all the way carry plus very assimmetrical numbers
    a = D(1)  # 1
    b = D(9, D(9, D(9, D(9))))  # 9999
    assert add(a, b).toInt() == 10000
    assert add(b, a).toInt() == 10000
