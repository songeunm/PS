# 2×n 타일링 2
# dp

import sys
input = sys.stdin.readline

def dp (n: int):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    memo = [0 for i in range(n + 1)]
    memo[1] = 1
    memo[2] = 3
    
    for i in range(3, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2] * 2
    return memo[-1]

if __name__ == "__main__":
    n = int(input())
    result = dp(n)
    print(result % 10007)