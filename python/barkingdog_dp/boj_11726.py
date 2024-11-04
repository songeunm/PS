# 2×n 타일링
# dp

import sys
input = sys.stdin.readline

def dp(n: int):
    d = [0 for i in range(n + 1)]
    if n == 1:
        return 1
    elif n == 2:
        return 2
    d[1] = 1
    d[2] = 2

    for i in range(3, n + 1):
        d[i] = d[i - 1] + d[i - 2]

    # print(d)
    return d[-1]


if __name__ == "__main__":
    n = int(input())

    result = dp(n) % 10007
    print(result)