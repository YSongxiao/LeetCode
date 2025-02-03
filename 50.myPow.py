class Solution:
    def myPow(self, x: float, n: int) -> float:
        def binpow(a, b):
            # 快速幂算法
            res = 1
            while b > 0:
                if b & 1:
                    res = res * a
                a = a * a
                b >>= 1
            return res
        if x == 1:
            return 1.0
        elif x == 0:
            return 0.0
        elif n == 0:
            return 1.0
        else:
            if n > 0:
                res = binpow(x, n)
            else:
                res = 1.0 / binpow(x, -n)
        return res


sol = Solution()
x = 2.00000
n = -2
print(sol.myPow(x, n))