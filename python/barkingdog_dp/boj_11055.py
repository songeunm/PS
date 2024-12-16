# 가장 큰 증가하는 부분 수열
# dp

import sys
input = sys.stdin.readline

def dp (seq: list):
    n = len(seq)
    memo = [seq[i] for i in range(n)]
    res = seq[0]

    for i in range(1, n):
        max_val = 0
        for j in range(0, i):
            if seq[j] < seq[i]:
                value = memo[j] + seq[i]
                if value > max_val:
                    max_val = value
                memo[i] = max_val
        if memo[i] > res:
            res = memo[i]
    # print(*memo)
    return res

if __name__ == "__main__":
    n = int(input())
    seq = list(map(int, input().split()))

    result = dp(seq)
    print(result)