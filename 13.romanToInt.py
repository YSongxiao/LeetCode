class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        special_dict = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        M = len(s)
        num_int = 0
        num = 0
        while num < M:
            if (num + 1) < M and s[num: num+2] in special_dict:
                num_int += special_dict[s[num: num+2]]
                num += 2
            else:
                num_int += dict[s[num]]
                num += 1
            # elif (num + 1) < M and s[num: num+2] not in special_dict:
            #     num_int += dict[s[num]]
            #     num += 1
            # elif (num + 1) >= M:
            #     num_int += dict[s[num]]
            #     break
        return num_int


solution = Solution()
s = "IX"
print(solution.romanToInt(s))