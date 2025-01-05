from typing import List

class Solution:
    def __init__(self):
        self.res = []

    def restoreIpAddresses(self, s: str) -> List[str]:
        self.restore("", 0, s)
        return self.res

    def restore(self, prefix, num, s):
        current_num = ""
        if num == 3 and len(s) > 3:
            return
        elif num == 3 and len(s) <= 3:
            if s[0] == "0" and len(s) > 1:
                return
            if 0 <= eval(s) <= 255:
                prefix += s
                self.res.append(prefix)
                return
            else:
                return
        for i in range(len(s)):
            if s[i] == "0" and current_num == "":
                current_num = "0"
                if num < 3:
                    if i + 1 < len(s):
                        self.restore(prefix+current_num+".", num+1, s[i+1:])
                        return
                    else:
                        return
                elif num == 3:
                    if len(s) > 1:
                        return
                    else:
                        self.res.append(prefix+current_num)
                        return
            else:
                current_num += s[i]
                if 0 <= eval(current_num) <= 255:
                    if num < 3:
                        if i + 1 < len(s) or (4-num) <= (len(s)-i-1) <= (4-num)*3:
                            self.restore(prefix+current_num+".", num+1, s[i+1:])
                        else:
                            continue



solution = Solution()
# s = "25525511135"
s = "0000"
# s = "101023"
print(solution.restoreIpAddresses(s))
