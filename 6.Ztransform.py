class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = ["" for _ in range(numRows)]
        if numRows == 1:
            return s
        else:
            loop = [i for i in range(numRows-1)] + [j for j in range(numRows-1, 0, -1)]
        for num, alphabet in enumerate(s):
            res[loop[num % (2 * numRows - 2)]] += (alphabet)
        res_str = ""
        for substring in res:
            res_str += substring
        return res_str


if __name__ == '__main__':
    string = "PAYPALISHIRING"
    numRow = 1
    solution = Solution()
    res = solution.convert(string, numRows=numRow)
    print(res)