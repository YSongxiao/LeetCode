class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        lv1 = len(v1)
        lv2 = len(v2)
        for i in range(max(lv1, lv2)):
            if i < min(lv1, lv2):
                if self.Str2Int(v1[i]) < self.Str2Int(v2[i]):
                    return -1
                elif self.Str2Int(v1[i]) > self.Str2Int(v2[i]):
                    return 1
            elif i >= lv1:
                if 0 < self.Str2Int(v2[i]):
                    return -1
            elif i >= lv2:
                if 0 < self.Str2Int(v1[i]):
                    return 1
        return 0

    def Str2Int(self, s):
        int_num = 0
        for i in range(len(s)):
            int_num += eval(s[i])
            int_num *= 10
        return int_num



sol = Solution()
version1 = "1.0.1"
version2 = "1"
print(sol.compareVersion(version1, version2))

