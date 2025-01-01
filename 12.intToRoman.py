class Solution:
    def intToRoman(self, num: int) -> str:
        dict = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M", 4: "IV", 9: "IX", 40: "XL", 90: "XC", 400: "CD", 900: "CM"}
        roman = ""
        str_num = str(num)
        if len(str_num) < 4:
            str_num = "0"*(4-len(str_num)) + str_num
        thousands = int(str_num[0])
        hundreds = int(str_num[1])
        tens = int(str_num[2])
        ones = int(str_num[3])
        roman += dict[1000] * thousands
        if hundreds == 4 or hundreds == 9:
            roman += dict[hundreds * 100]
        elif hundreds >= 5:
            roman += dict[500]
            roman += dict[100] * (hundreds - 5)
        else:
            roman += dict[100] * hundreds
        if tens == 4 or tens == 9:
            roman += dict[tens * 10]
        elif tens >= 5:
            roman += dict[50]
            roman += dict[10] * (tens - 5)
        else:
            roman += dict[10] * tens
        if ones == 4 or ones == 9:
            roman += dict[ones * 1]
        elif ones >= 5:
            roman += dict[5]
            roman += dict[1] * (ones - 5)
        else:
            roman += dict[1] * ones
        return roman


solution = Solution()
num = 3749
print(solution.intToRoman(num))
# 其实还可以直接把所有数字做成一个表然后直接映射