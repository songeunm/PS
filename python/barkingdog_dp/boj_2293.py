# 동전 1

import sys
input = sys.stdin.readline

def dp(coins: list, k: int):
    n = len(coins)
    memo = [0 for i in range(k + 1)] # i원을 만드는 경우의 수
    memo[0] = 1

    for coin in coins:
        for i in range(1, k + 1):
            if i - coin >= 0:
                memo[i] += memo[i - coin]

    # print(* memo)
    return memo[-1]

if __name__ == "__main__":
    n, k = map(int, input().split())

    coins = []
    for i in range(n):
        coins.append( int(input()) )
    
    result = dp(coins, k)
    print(result)