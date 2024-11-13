# 정수 삼각형
# dp

import sys
input = sys.stdin.readline

def dp (t: list):
    n = len(t)
    if n == 1:
        return t[0][0]

    memo = [[0 for i in range(j + 1)] for j in range(n)]
    memo[n - 1] = t[n - 1]

    for i in range(n - 2, -1, -1):
        for j in range(i + 1):
            memo[i][j] = t[i][j] + max(memo[i + 1][j], memo[i + 1][j + 1])
    
    # print(memo)
    return memo[0][0]


if __name__ == "__main__":
    n = int(input())
    triangle = []
    for i in range(n):
        nums = list(map(int, input().split()))
        triangle.append(nums)
    result = dp(triangle)
    print(result)