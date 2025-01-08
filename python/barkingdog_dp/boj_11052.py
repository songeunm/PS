# 카드 구매하기
# dp

import sys
input = sys.stdin.readline

def dp(cp, n):
    # memo[i]: i개의 카드를 모을 때 가장 최대 소비
    memo = [0] + cp

    for i in range(2, n + 1):
        max_value = memo[i]
        for j in range(0, i // 2 + 1):
            if max_value < memo[j] + memo[i-j]:
                max_value = memo[j] + memo[i-j]
                # print(f"changed: memo[{i}] = {memo[j]} + {memo[i-j]} = {max_value}")
        memo[i] = max_value

    # print(*memo)
    return memo[-1]


if __name__ == "__main__":
    n = int(input())
    card_pack = list(map(int, input().split()))

    result = dp(card_pack, n)
    print(result)