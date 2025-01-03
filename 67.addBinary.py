class Solution:
    def addBinary(self, a: str, b: str) -> str:
        N1 = len(a)
        N2 = len(b)
        longer = a[::-1] if N1 >= N2 else b[::-1]
        shorter = b[::-1] if N1 >= N2 else a[::-1]
        increase = 0
        i = 0
        result = ""
        while i < max(N1, N2) or increase > 0:
            if i < min(N1, N2):
                tmp = int(longer[i]) + int(shorter[i]) + increase
                increase = tmp // 2
                result += str(tmp % 2)
                i+=1
            elif max(N1, N2) > i >= min(N1, N2):
                if increase == 0:
                    result += longer[i:]
                    break
                else:
                    tmp = int(longer[i]) + increase
                    increase = tmp // 2
                    result += str(tmp % 2)
                    i += 1
            else:
                result += str(increase)
                break
        return result[::-1]


solution = Solution()
a = "100"
b = "110010"
print(solution.addBinary(a,b))