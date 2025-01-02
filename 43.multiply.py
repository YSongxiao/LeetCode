class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def reversed_add(num1, num2):
            N1, N2 = len(num1), len(num2)
            long_num = num1 if N1 > N2 else num2
            short_num = num2 if N1 > N2 else num1
            result = ""
            increase = 0
            i = 0
            while i < max(N1, N2) or increase > 0:
                if i >= max(N1, N2):
                    result += str(increase)
                    break
                elif i >= min(N1, N2):
                    tmp_result = int(long_num[i]) + increase
                    increase = tmp_result // 10
                    tmp_result = tmp_result % 10
                    result += str(tmp_result)
                    i += 1
                else:
                    tmp_result = int(long_num[i]) + int(short_num[i]) + increase
                    increase = tmp_result // 10
                    tmp_result = tmp_result % 10
                    result += str(tmp_result)
                    i += 1
            return result
        # print(''.join(reversed(reversed_add("991", "111"))))
        if num1 == '0' or num2 == '0':
            return "0"
        N1 = len(num1)
        N2 = len(num2)
        result = "0"
        for i in range(N2-1, -1, -1):
            increase = 0
            tmp_result = ""
            for j in range(N1-1, -1, -1):
                tmp = increase + int(num2[i]) * int(num1[j])
                increase = tmp // 10
                ones = tmp % 10
                tmp_result += str(ones)
                if j == 0 and increase > 0:
                    tmp_result += str(increase)
            tmp_result = "0" * (N2-1-i) + tmp_result
            result = reversed_add(result, tmp_result)
        result = ''.join(reversed(result))
        return result

solution = Solution()
num1 = "123"
num2 = "456"
print(solution.multiply(num1, num2))