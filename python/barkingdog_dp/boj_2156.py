# 포도주 시식

import sys
input = sys.stdin.readline

def dp (lst: list):
    n = len(lst)
    if n == 1:
        return lst[0]
    elif n == 2:
        return lst[0] + lst[1]

    # memo[i]: i번째 잔을 마신다고 가정할 때 맛볼수 있는 최대 포도주 양
    memo = [0 for i in range(n)]
    memo[0] = lst[0]
    memo[1] = lst[0] + lst[1]
    memo[2] = max(lst[0] + lst[1], lst[1] + lst[2], lst[0] + lst[2])

    for i in range(3, n):
        val_1 = lst[i-1] + memo[i - 3]
        val_2 = memo[i - 2]
        val_3 = lst[i-1] + memo[i - 4]
        memo[i] = max(val_1, val_2, val_3) + lst[i]

    # print(* memo)
    return max(memo)

if __name__ == "__main__":
    n = int(input())

    wine = []
    for i in range(n):
        w = int(input())
        wine.append(w)
    
    result = dp(wine)
    print(result)