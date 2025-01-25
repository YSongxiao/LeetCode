class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dicts = dict()
        dictt = dict()
        for i in range(len(s)):
            if dicts.get(s[i]) is None and dictt.get(t[i]) is None:
                dicts[s[i]] = t[i]
                dictt[t[i]] = s[i]
            elif s[i] in dicts and t[i] in dictt:
                if dicts[s[i]] != t[i] or dictt[t[i]] != s[i]:
                    return False
            else:
                return False
        return True


sol = Solution()
s = "badc"
t = "baba"
print(sol.isIsomorphic(s, t))