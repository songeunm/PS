# 파도반 수열
# dp

import sys
input = sys.stdin.readline

def dp (n: int):
    if n <= len(memo):
        return memo[n - 1]
    
    i = len(memo)
    while i != n:
        memo.append( memo[i - 1] + memo[i - 5] )
        i += 1
    # print(*memo)
    return memo[i - 1]

if __name__ == "__main__":
    t = int(input())
    memo = [1, 1, 1, 2, 2]

    for testcase in range(t):
        n = int(input())
        print( dp(n) )
        