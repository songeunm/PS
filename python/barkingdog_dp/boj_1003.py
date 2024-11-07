# 피보나치 함수
# dp

import sys
input = sys.stdin.readline

def fibonacci(n: int):
    if n == 0:
        print("0")
        return 0
    elif n == 1:
        print("1")
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def dp (n: int):
    if n == 0:
        return 1, 0
    elif n == 1:
        return 0, 1
    memo = [(0, 0) for i in range(n+1)]
    memo[0] = (1, 0)
    memo[1] = (0, 1)

    for x in range(2, n+1):
        val_1 = memo[x - 1][0] + memo[x - 2][0]
        val_2 = memo[x - 1][1] + memo[x - 2][1]
        memo[x] = (val_1, val_2)
    # print(memo)
    return memo[n]


if __name__ == "__main__":
    t = int(input())
    for testcase in range(t):
        n = int(input())
        result = dp(n)
        print(*result)