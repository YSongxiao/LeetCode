from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        M = len(s)
        N = len(wordDict)
        dp = [[[False]] * N for _ in range(M)]
        current_words = [""]
        flag = False
        for i in range(M):
            for num, _ in enumerate(current_words):
                current_words[num] += s[i]
            for j in range(N):
                if wordDict[j] in current_words:
                    dp[i][j][0] = True
                    flag = True
                    if i == M-1:
                        return True
            if flag:
                current_words.append("")
                flag = False
        return False

    def wordBreak_1(self, s: str, wordDict: List[str]) -> bool:
        M = len(s)
        dp = [False] * (M+1)
        dp[0] = True
        for i in range(M):
            for j in range(i+1, M+1):
                if dp[i] and (s[i:j] in wordDict):
                    dp[j] = True
        return dp[-1]


solution = Solution()
# s = "leetcode"
s = "catsandog"
# wordDict = ["leet", "code"]
wordDict = ["cats", "dog", "sand", "and", "cat"]
print(solution.wordBreak_1(s, wordDict))