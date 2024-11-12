# 높은 곳으로
# dp

import sys
input = sys.stdin.readline

def dp (n, p):
    r = n * (n + 1) // 2
    f = 0
    for i in range(1, n + 1):
        f += i
        if f == p:
            return r - 1
    return r

if __name__ == "__main__":
    t = int(input())
    for testcase in range(t):
        n, p = map(int, input().split())

        result = dp(n, p)
        print(result)