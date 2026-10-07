class Solution(object):
    def myAtoi(self, s):
        i = 0
        n = len(s)

        # Ignore leading spaces
        while i < n and s[i] == ' ':
            i += 1

        # Check sign
        sign = 1

        if i < n and s[i] == '-':
            sign = -1
            i += 1
        elif i < n and s[i] == '+':
            i += 1

        # Convert digits
        result = 0

        while i < n and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')
            result = result * 10 + digit
            i += 1

        result *= sign

        # 32-bit integer range
        if result < -2**31:
            return -2**31

        if result > 2**31 - 1:
            return 2**31 - 1

        return result