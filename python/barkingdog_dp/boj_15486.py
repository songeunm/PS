# 퇴사 2
# dp greedy

import sys
input = sys.stdin.readline

def dp (n: int, time: list, price: list):
    memo = [0 for i in range(n + 1)]
    if n == 1:
        if time[0] > 1:
            return 0
        else:
            return price[0]
    
    if time[n - 1] > 1:
        memo[n - 1] = 0
    else:
        memo[n - 1] = price[n - 1]
    for i in range(n - 2, -1, -1):
        if i + time[i] - 1 < n:
            memo[i] = max(memo[i + 1], memo[i + time[i]] + price[i])
        else:
            memo[i] = memo[i + 1]
    # print(memo)
    return memo[0]

if __name__ == "__main__":
    n = int(input())
    time = []
    price = []
    for i in range(n):
        t, p = map(int, input().split())
        time.append(t)
        price.append(p)
    
    result = dp(n, time, price)
    print(result)