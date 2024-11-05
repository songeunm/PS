# 구간 합 구하기 4
# dp

import sys
input = sys.stdin.readline

def dp (i: int, j: int, cur: int, n_num: list, memo: list):
    if cur >= j:
        return cur

    for x in range(cur + 1, j + 1):
        memo[x] = memo[x - 1] + n_num[x]
        cur += 1
    
    return cur

if __name__ == "__main__":
    n, m = map(int, input().split())
    n_num = list(map(int, input().split()))
    n_num.insert(0, 0)
    memo = [0 for i in range(n + 1)]
    cur = 0

    for k in range(m):
        i, j = map(int, input().split())
        
        cur = dp(i, j, cur, n_num, memo)
        result = memo[j] - memo[i - 1]
        print(result)