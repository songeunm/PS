# 퇴사
# DP

import sys
input = sys.stdin.readline

def dp (time: list, price: list):
    n = len(time)
    memo = [0 for i in range(n)]
    if time[-1] == 1:
        memo[-1] = price[-1]
    else:
        memo[-1] = 0
    
    i = n - 2
    while i >= 0:
        if i + time[i] < n:
            memo[i] = max(memo[i + 1], memo[i + time[i]] + price[i])
        elif i + time[i] == n:
            memo[i] = max(memo[i + 1], price[i])
        else:
            memo[i] = memo[i + 1]
        i -= 1
    # print(* memo)
    return memo[0]

if __name__ == "__main__":
    n = int(input())
    time = []
    price = []
    for i in range(n):
        t, p = map(int, input().split())
        time.append(t)
        price.append(p)
    
    result = dp(time, price)
    print(result)