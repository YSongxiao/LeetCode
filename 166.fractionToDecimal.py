class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        res = ""
        symbol = "" if numerator * denominator >= 0 else "-"
        integer, tmp_remainder = divmod(abs(numerator), abs(denominator))
        res += symbol + str(integer)
        if tmp_remainder != 0:
            res += "."
        remainder = ""
        remainders = dict()
        pos = 0
        while tmp_remainder != 0:
            integer, tmp_remainder = divmod(tmp_remainder*10, abs(denominator))
            if (integer, tmp_remainder) in dict(remainders):
                idx = remainders[(integer, tmp_remainder)]
                cycle = remainder[idx:]
                return res + remainder[:idx] + "(" + cycle + ")"
            else:
                remainders.update({(integer, tmp_remainder): pos})
            remainder += str(integer)
            pos += 1
        return res + remainder


sol = Solution()
numerator = 7
denominator = -12
print(sol.fractionToDecimal(numerator, denominator))