# 이친수
# dp

import sys
input = sys.stdin.readline

def dp (n: int):
    if n == 1 or n == 2:
        return 1
    
    memo = [(0,0) for i in range(n + 1)]
    memo[1] = (0, 1)
    memo[2] = (1, 0)
    for i in range(3, n + 1):
        memo[i] = (memo[i - 1][0] + memo[i -  1][1], memo[i - 1][0])
    
    # print(memo)
    res = sum(memo[n])
    return res


if __name__ == "__main__":
    n = int(input())
    result = dp(n)
    print(result)