# Given two binary strings a and b, return their sum as a binary string.

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"

# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"

class Solution:
    # 1-based right-to-left string chars addressing. If index overflows, returns 0
    def safe_bin_address(self, s: str, pos: int) -> int:
        if pos <= len(s):
            ch = s[-pos]
            if ch == '0':
                return 0
            else:
                return 1
        return 0

    def addBinary(self, a: str, b: str) -> str:
        posa = 1
        posb = 1
        carry = 0
        ret_val = ''
        while posa <= len(a) or posb <= len(b):
            temp = self.safe_bin_address(a, posa) + \
                self.safe_bin_address(b, posb) + carry
            if temp == 0:
                ret_val = '0'+ret_val
                carry = 0
            elif temp == 1:
                ret_val = '1' + ret_val
                carry = 0
            elif temp == 2:
                ret_val = '0' + ret_val
                carry = 1
            else:  # temp == 3
                ret_val = '1' + ret_val
                carry = 1

            posa += 1
            posb += 1

        if carry == 1:
            ret_val = '1' + ret_val

        return ret_val


def test_addBinary():
    s = Solution()
    assert s.addBinary('0', '0') == '0'
    assert s.addBinary('1', '0') == '1'
    assert s.addBinary('1', '1') == '10'
    assert s.addBinary('11', '1') == '100'
    assert s.addBinary('1011', '1') == '1100'
