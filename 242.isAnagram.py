class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicts = {}
        dictt = {}
        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                if s[i] in dicts:
                    dicts[s[i]] += 1
                else:
                    dicts[s[i]] = 1
                if t[i] in dictt:
                    dictt[t[i]] += 1
                else:
                    dictt[t[i]] = 1
            for key in sorted(dicts.keys()):
                if dicts[key] != dictt.get(key, None):
                    return False
            return True


sol = Solution()
s = "rat"
t = "car"
print(sol.isAnagram(s, t))
