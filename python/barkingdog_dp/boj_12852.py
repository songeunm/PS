# 1로 만들기 2
# dp

import sys
input = sys.stdin.readline

def dp (n: int):
    memo = [0 for i in range(n + 1)]
    seq = [[] for i in range(n + 1)]
    if n == 1:
        return 0, [1]
    elif n == 2 or n == 3:
        return 1, [n, 1]
    memo[2] = 1
    memo[3] = 1
    seq[1] = [1]
    seq[2] = [2, 1]
    seq[3] = [3, 1]

    for x in range(4, n + 1):
        calc = [(memo[x - 1], x - 1)]
        if x % 3 == 0:
            calc.append((memo[x // 3], x // 3))
        if x % 2 == 0:
            calc.append((memo[x // 2], x // 2))
        min_value, m_idx = min(calc, key=lambda x: x[0])
        memo[x] = min_value + 1
        seq[x] = [x] + seq[m_idx]

    return memo[n], seq[n]

if __name__ == "__main__":
    n = int(input())
    
    result, seq = dp(n)
    print(result)
    print(*seq)