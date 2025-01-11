class Solution:
    def numDecodings(self, s: str) -> int:
        self.dict = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26"}
        dp = [[0] * 2 for _ in range(len(s))]
        dp[0][0] = 1 if s[0] in self.dict else 0
        dp[0][1] = 0
        for i in range(1, len(s)):
            if s[i] in self.dict:
                dp[i][0] = dp[i - 1][0] + dp[i - 1][1]
            else:
                dp[i][0] = 0
            if s[i-1: i+1] in self.dict:
                dp[i][1] = dp[i-1][0]
            else:
                dp[i][1] = 0
        return dp[len(s) - 1][0] + dp[len(s) - 1][1]

solution = Solution()
# s = "12"
s = "10"
print(solution.numDecodings(s))