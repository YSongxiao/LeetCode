from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.M = len(s)
        self.res = []
        self.ans = []
        self.s = s
        self.dp = [[True] * self.M for _ in range(self.M)]
        for i in range(self.M-1, -1, -1):
            for j in range(i+1, self.M):
                self.dp[i][j] = (self.s[i] == self.s[j]) and self.dp[i+1][j-1]
        self.dfs(0)
        return self.res

    def dfs(self, i):
        if i == self.M:
            self.res.append(self.ans[:])
            return
        else:
            for j in range(i, self.M):
                if self.dp[i][j]:
                    self.ans.append(self.s[i:j+1])
                    self.dfs(j+1)
                    self.ans.pop()
                # Without DP preprocessing, use below
                # if self.isValid(self.s[i:j+1]):
                #     self.ans.append(self.s[i:j+1])
                #     self.dfs(j+1)
                #     self.ans.pop()

    def isValid(self, string: str) -> bool:
        N = len(string)
        start = 0
        end = N - 1
        while start < end:
            if string[start] == string[end]:
                start += 1
                end -= 1
            else:
                return False
        return True


solution = Solution()
# s = "aab"
s = "abbab"
print(solution.partition(s))