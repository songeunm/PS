# 1로 만들기
# dp

import sys
input = sys.stdin.readline

def dp (n: int):
    memo = [0 for i in range(n+1)]
    if n == 1:
        return 0
    elif 1 < n <= 3:
        return 1
    x = 2
    while x <= n:
        case_1 = memo[x // 3] if x % 3 == 0 else float('inf')
        case_2 = memo[x // 2] if x % 2 == 0 else float('inf')
        case_3 = memo[x - 1]
        memo[x] = min(case_1, case_2, case_3) + 1
        x += 1
    # print(memo)
    return memo[n]

if __name__ == "__main__":
    n = int(input())
    result = dp(n)
    print(result)