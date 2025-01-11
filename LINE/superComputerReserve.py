import sys

failed = []

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
    num_req = eval(lines[2])
    for i in range(num_req):
        tmp_line = lines[i+3].split(" ")
        start = eval(tmp_line[0])
        end = eval(tmp_line[1])
        if failed:
            for fail in failed:
                if start >= fail[0] and fail[1] >= end:
                    print(-1)
                    break
                elif start >= fail[0] and end < fail[1]:
                    find_slot(unava, fail[1], end, 0, len(unava) - 1, start, end)
                    break
                else:
                    find_slot(unava, start, end, 0, len(unava) - 1, start, end)
                    break
        else:
            find_slot(unava, start, end, 0, len(unava) - 1, start, end)

def find_nearest(lis, num, start_idx, end_idx):
    for i in range(start_idx, end_idx+1):
        if num > lis[i]:
            continue
        else:
            return i
    return end_idx


def find_slot(lis, start, end, lis_start, lis_end, ori_start, ori_end):
    idx = find_nearest(lis, start, lis_start, lis_end)
    if lis[idx] == start:
        start = start + 1
        if start > end:
            print(-1)
            failed.append([ori_start, ori_end])
            return
        else:
            while lis[idx+1] == start:
                idx += 1
                start += 1
                if start > end:
                    print(-1)
                    failed.append([ori_start, ori_end])
                    return
            find_slot(lis, start, end, idx, lis_end, ori_start, ori_end)
    else:
        print(start)
        return

if __name__ == '__main__':
    lines = ["10 5", "3 4 6 7 8", "3", "1 1", "3 7", "6 8"]
    main(lines)