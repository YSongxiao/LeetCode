import sys
import numpy as np

class Program:
    def __init__(self, n, q, MAXA, MAXV, seed, threshold):
        self.state = seed
        self.n = n
        self.q = q
        self.MAXA = MAXA
        self.MAXV = MAXV
        self.threshold = threshold
# state = seed
    def rnd(self):
        self.state = (self.state * 1564328749 + 12345) % (2 ** 31)
        return self.state

    def run(self):
        a = []
        command = ["" for _ in range(self.q)]
        for i in range(self.n):
            a.append((self.rnd() % self.MAXA) + 1)

        for query_number in range(self.q):
            if self.rnd() < self.threshold:
                l = (self.rnd() % self.n)
                r = (self.rnd() % self.n)
                v = (self.rnd() % self.MAXV) + 1
                if l > r:
                    tmp = l
                    l = r
                    r = tmp
                    # swap(l, r)
                command[query_number] = f"B {l} {r} {v}"
                # // query_number 番目のクエリは、"B l r v"
            else:
                i = (self.rnd() % self.n)
                x = (self.rnd() % self.MAXA) + 1
                command[query_number] = f"A {i} {x}"
                # // query_number 番目のクエリは、"A i x"
        return a, command


def commandA(a, i, x):
    a[i] = x
    return a


def commandA_(a, i, x, prefix, MAXV, n):
    ori = a[i]
    a[i] = x
    for v_ in range(2, MAXV+1):
        if ori % v_ == 0 and x % v_ != 0:
            prefix[v_ - 1, i+1:] -= 1

            # for n_ in range(i + 1, n + 1):
            #     prefix[v_-1][n_] -= 1
        elif ori % v_ != 0 and x % v_ == 0:
            prefix[v_ - 1, i+1:] += 1

            # for n_ in range(i + 1, n + 1):
            #     prefix[v_-1][n_] += 1
    return a, prefix


def commandB(a, l, r, v):
    num = 0
    for i in range(l, r+1):
        if a[i] % v == 0:
            num += 1
    return num


def commandB_(a, prefix, l, r, v):
    num = prefix[v-1, r+1] - prefix[v-1, l]
    return num


def initial(a, prefix, MAXV, n):
    for v_ in range(1, MAXV+1):
        for n_ in range(1, n+1):
            if a[n_-1] % v_ == 0:
                prefix[v_-1, n_] = prefix[v_-1, n_-1] + 1
            else:
                prefix[v_-1, n_] = prefix[v_-1, n_-1]
    return prefix


def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.
    tmp_line = lines[0].split(" ")
    n = eval(tmp_line[0])
    q = eval(tmp_line[1])
    tmp_line = lines[1].split(" ")
    MAXA = eval(tmp_line[0])
    MAXV = eval(tmp_line[1])
    tmp_line = lines[2].split(" ")
    seed = eval(tmp_line[0])
    threshold = eval(tmp_line[1])
    program = Program(n, q, MAXA, MAXV, seed, threshold)
    a, command = program.run()
    result = 0
    prefix = np.zeros((MAXV, n + 1), dtype=int)
    # prefix = np.array([[0 for _ in range(n+1)] for _ in range(MAXV)])
    prefix = initial(a, prefix, MAXV, n)
    for com in command:
        if com[0] == "A":
            tmpline = com.split(" ")
            i = eval(tmpline[1])
            x = eval(tmpline[2])
            # a = commandA(a, i, x)
            a, prefix = commandA_(a, i, x, prefix, MAXV, n)
        else:
            tmpline = com.split(" ")
            l = eval(tmpline[1])
            r = eval(tmpline[2])
            v = eval(tmpline[3])
            # result += commandB(a, l, r, v)
            result += commandB_(a, prefix, l, r, v)
    print(result)


if __name__ == '__main__':
    lines = ["5 5", "5 3", "54364 1200000000"]
    # for l in sys.stdin:
    #     lines.append(l.rstrip('\r\n'))
    main(lines)