# 극장 좌석

import sys
input = sys.stdin.readline

def dp (n: int, lst: list):
    # memo[i][0]: i번째 좌석까지 앉을 때 i번째 자리에 본인이 앉는 경우 앉을 수 있는 방법 가짓수
    # memo[i][1]: i번째 좌석까지 앉을 때 i번째 자리에 본인이 앉지 않는 경우 앉을 수 있는 방법 가짓수
    memo = [[0, 0] for i in range(n)]
    memo[0] = [1, 0]

    j = 0 # lst의 idx
    for i in range(1, n):
        if j < len(lst):
            if i == lst[j]:
                memo[i] = [sum(memo[i - 1]), 0]
                continue
            elif i == lst[j] + 1:
                memo[i] = [sum(memo[i - 1]), 0]
                j += 1
                continue
        memo[i] = [sum(memo[i - 1]), memo[i - 1][0]]
    
    # print(* memo)
    return sum(memo[-1])

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    
    vip = []
    for i in range(m):
        num = int(input()) - 1
        vip.append(num)
    
    result = dp(n, vip)
    print(result)