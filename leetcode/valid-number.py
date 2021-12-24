# https://leetcode.com/problems/valid-number/
# A valid number can be split up into these components ( in order):

# A decimal number or an integer.
# (Optional) An 'e' or 'E', followed by an integer.
# A decimal number can be split up into these components ( in order):

# (Optional) A sign character(either '+' or '-').
# One of the following formats:
# One or more digits, followed by a dot '.'.
# One or more digits, followed by a dot '.', followed by one or more digits.
# A dot '.', followed by one or more digits.
# An integer can be split up into these components ( in order):

# (Optional) A sign character(either '+' or '-').
# One or more digits.
# For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

# Given a string s, return true if s is a valid number.

import re


class Solution:
    def isNumber(self, s: str) -> bool:
        ret_val = True
        if s is None or len(s) == 0:
            return False
        split_s = re.split('e|E', s)
        if len(split_s) > 2:
            return False
        elif len(split_s) == 2:
            ret_val = self.is_signed_integer(split_s[1])
        return ret_val and self.is_signed_decimal(split_s[0])

    def is_integer(self, s: str) -> bool:
        if s is None or len(s) == 0:
            return False
        for ch in s:
            if not ch.isdigit():
                return False
        return True

    def is_signed_integer(self, s: str) -> bool:
        if s is None or len(s) == 0:
            return False
        # if the first char is sign or digit, ...
        if s[0] in ['+', '-']:
            return self.is_integer(s[1:])  # ... process the rest of it
        return self.is_integer(s)  # otherwise, try parse it all

    def is_decimal(self, s: str) -> bool:
        if s is None or len(s) == 0:
            return False

        split_s = re.split('\.|,', s)
        if len(split_s) > 2:
            return False
        if len(split_s) == 2:

            if len(split_s[0]) == 0:  # .1 is allowed
                return self.is_integer(split_s[1])
            elif len(split_s[1]) == 0:  # 12. is allowed
                return self.is_integer(split_s[0])
            else:  # case both parts present, like 12.34
                return self.is_integer(split_s[0]) and self.is_integer(split_s[1])

        else:  # case of the integer
            return self.is_integer(s)

    def is_signed_decimal(self, s: str) -> bool:
        if s is None or len(s) == 0:
            return False
        if s[0] in ['+', '-']:
            return self.is_decimal(s[1:])
        return self.is_decimal(s)


def test_is_integer():
    s = Solution()
    assert s.is_integer(None) == False
    assert s.is_integer('') == False
    assert s.is_integer('4') == True
    assert s.is_integer('423523') == True
    assert s.is_integer('423.523') == False
    assert s.is_integer('a123') == False
    assert s.is_integer('12345e11') == False
    assert s.is_integer('+12') == False
    assert s.is_integer('-34') == False
    assert s.is_integer('+123'[1:]) == True  # taking out the sign


def test_is_signed_integer():
    s = Solution()
    assert s.is_signed_integer(None) == False
    assert s.is_signed_integer('') == False
    assert s.is_signed_integer('4') == True
    assert s.is_signed_integer('423523') == True
    assert s.is_signed_integer('423,523') == False
    assert s.is_signed_integer('a123') == False
    assert s.is_signed_integer('12345e11') == False
    assert s.is_signed_integer('+12') == True
    assert s.is_signed_integer('-34') == True
    assert s.is_signed_integer('+123'[1:]) == True  # taking out the sign


def test_is_decimal():
    s = Solution()
    assert s.is_decimal(None) == False
    assert s.is_decimal('') == False
    assert s.is_decimal('0') == True
    assert s.is_decimal('423523') == True
    assert s.is_decimal('a123') == False
    assert s.is_decimal('12345e11') == False
    assert s.is_decimal('+12') == False
    assert s.is_decimal('+123'[1:]) == True  # taking out the sign
    assert s.is_decimal('123.') == True
    assert s.is_decimal('123.45') == True
    assert s.is_decimal('123,45') == True
    assert s.is_decimal('123.+12') == False
    assert s.is_decimal('-15.0') == False
    assert s.is_decimal('.1') == True


def test_is_signed_decimal():
    s = Solution()
    assert s.is_signed_decimal(None) == False
    assert s.is_signed_decimal('') == False
    assert s.is_signed_decimal('0') == True
    assert s.is_signed_decimal('423523') == True
    assert s.is_signed_decimal('a123') == False
    assert s.is_signed_decimal('12345e11') == False
    assert s.is_signed_decimal('+12') == True
    assert s.is_signed_decimal('-34') == True
    assert s.is_signed_decimal('+123'[1:]) == True  # taking out the sign
    assert s.is_signed_decimal('123.') == True
    assert s.is_signed_decimal('123.45') == True
    assert s.is_signed_decimal('123,45') == True
    assert s.is_signed_decimal('123.+12') == False
    assert s.is_signed_decimal('-15.0') == True
    assert s.is_signed_decimal('.1') == True


def test_isNumber():
    s = Solution()
    assert s.isNumber('0') == True
    assert s.isNumber('.1') == True
    assert s.isNumber('+.1') == True


test_is_integer()
test_is_signed_integer()
test_is_decimal()
test_isNumber()
