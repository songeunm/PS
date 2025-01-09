# 01타일
# dp

import sys
input = sys.stdin.readline

def dp(n: int):
    # memo[i]: i자릿수의 2진수를 만들 수 있는 경우의 수
    # n <= 1000,000 이기 때문에 memo[i] 계산에 필요한 memo[i-1], memo[i-2]만 저장
    if n == 1:
        return 1
    elif n == 2:
        return 2
    memo_1 = 1
    memo_2 = 2

    for i in range(3, n+1):
        memo_2, memo_1 = (memo_1 + memo_2) % 15746, memo_2 % 15746
    
    return memo_2

if __name__ == "__main__":
    n = int(input())

    result = dp(n) % 15746
    print(result)
