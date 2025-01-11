import sys


class Solution:
    def __init__(self, unava, checked):
        self.unava = set(unava)
        self.checked = checked

    def find_min_available(self, num):
        if num in self.checked:
            return self.checked[num]
        else:
            tmp = self.find(num)
            self.checked[num] = tmp
            return tmp

    def find(self, num):
        if num in self.unava:
            return False
        else:
            return True


def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.
    tmp_line = lines[0].split(" ")
    len_time = eval(tmp_line[0])
    num_unava = eval(tmp_line[1])
    tmp_line = lines[1].split(" ")
    unava = [eval(item) for item in tmp_line]
    checked = {}
    num_req = eval(lines[2])
    solution = Solution(unava, checked)
    for i in range(num_req):
        flag = 0
        tmp_line = lines[i + 3].split(" ")
        start = eval(tmp_line[0])
        end = eval(tmp_line[1])
        for j in range(start, end+1):
            if solution.find_min_available(j):
                print(j)
                flag = 1
                break
        if flag == 0:
            print(-1)


if __name__ == '__main__':
    lines = ["10 5", "3 4 6 7 8", "3", "1 1", "3 7", "6 8"]
    main(lines)
