class Solution(object):
    def divide(self, dividend, divisor):
        # Handle overflow case
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        # Determine the sign
        negative = (dividend < 0) != (divisor < 0)

        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        # Subtract using powers of 2
        while dividend >= divisor:
            temp = divisor
            multiple = 1

            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            dividend -= temp
            quotient += multiple

        if negative:
            quotient = -quotient

        return quotient