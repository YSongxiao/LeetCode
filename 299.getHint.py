class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        cows = 0
        bulls = 0
        unmatch_s = {}
        unmatch_g = {}
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                if guess[i] in unmatch_g:
                    unmatch_g[guess[i]] += 1
                else:
                    unmatch_g[guess[i]] = 1
                if secret[i] in unmatch_s:
                    unmatch_s[secret[i]] += 1
                else:
                    unmatch_s[secret[i]] = 1
        for key in unmatch_g:
            if key in unmatch_s:
                cows += min(unmatch_g[key], unmatch_s[key])
        return str(bulls) + 'A' + str(cows) + 'B'


sol = Solution()
secret = "1123"
guess = "0111"
print(sol.getHint(secret, guess))