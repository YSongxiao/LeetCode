class Solution:
    def reverse(self, x: int) -> int:
        # 主要在于如何判断正溢和负溢，用2**31 // 10的时候当前数字大小以及余数来判断即可。
        # 注意整数前面为0的情况
        INT_MAX = 2147483647
        sign = 1 if x >= 0 else -1
        x = abs(x)
        reversed_x = 0
        while x > 0:
            num = x % 10
            if num == 0 and reversed_x == 0:
                x = x // 10
                continue
            if reversed_x < INT_MAX // 10:
                reversed_x = reversed_x * 10 + num
            elif reversed_x == INT_MAX // 10:
                if num > 7 and sign == 1:
                    return 0
                elif num > 8 and sign == -1:
                    return 0
                else:
                    reversed_x = reversed_x * 10 + num
            else:
                return 0
            x = x // 10
        reversed_x = reversed_x if sign == 1 else -reversed_x
        return reversed_x


solution = Solution()
x = 1534236469
print(solution.reverse(x))