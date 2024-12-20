# 가장 긴 증가하는 부분 순열
# DP

import sys
input = sys.stdin.readline

def dp (lst: list):
    n = len(lst)
    # memo[i] : i번째 수까지의 i번째 수가 가장 큰 증가 부분 수열의 최대 길이
    memo = [0 for i in range(n)]

    for i in range(0, n):
        max_value = 0
        for j in range(0, i):
            if lst[j] < lst[i] and max_value < memo[j]:
                max_value = memo[j]
        memo[i] = max_value + 1
    
    # print( *memo )
    return max(memo)

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    
    result = dp(a)
    print(result)