class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            string = self.countAndSay(n-1)
            start_pos = 0
            end_pos = 0
            new_string = ""
            while end_pos <= len(string):
                if end_pos == len(string):
                    new_string += (str(end_pos - start_pos) + string[start_pos])
                    break
                if string[end_pos] == string[start_pos]:
                    end_pos += 1
                else:
                    new_string += (str(end_pos-start_pos) + string[start_pos])
                    start_pos = end_pos
            return new_string


if __name__ == '__main__':
    n = 1
    solution = Solution()
    res = solution.countAndSay(n)
    print(res)