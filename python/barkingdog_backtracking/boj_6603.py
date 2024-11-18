# 로또
# bt

import sys
input = sys.stdin.readline

lst = []

def bt (i: int, cur: int, s: list):
    if i == 6:
        print(*lst)
        return

    for idx in range(len(s)):
        if idx <= cur:
            continue
        lst.append(s[idx])
        bt(i + 1, idx, s)
        lst.pop()


if __name__ == "__main__":
    while 1:
        inp = list(map(int, input().split()))
        k = inp[0]
        if k == 0:
            break
        s = inp[1:]

        # print(f"s: {s}")
        bt(0, -1, s)
        print()