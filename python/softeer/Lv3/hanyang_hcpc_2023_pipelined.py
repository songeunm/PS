# pipelined

import sys

input = sys.stdin.readline

def pipeline(s: list):
    s.sort()
    i = 1
    time = 1
    cur_numerator = 1
    while i < len(s):
        cur = cur_numerator / s[i - 1]
        nxt = 1 / s[i]
        if nxt <= cur:
            cur = nxt
            i += 1
        else:
            cur_numerator += 1
        time += 1
    remain = s[-1] - 1
    return time + remain

if __name__ == "__main__":
    n = int(input())
    s = list(map(int, input().split()))

    result = pipeline(s)
    print(result)