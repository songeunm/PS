# RGB거리
# dp

import sys
input = sys.stdin.readline

def dp (cost: list):
    n = len(cost)
    paint = [[0, 0, 0] for i in range(n)]
    paint[0][0] = cost[0][0]
    paint[0][1] = cost[0][1]
    paint[0][2] = cost[0][2]

    for i in range(1, n):
        paint[i][0] = min(paint[i - 1][1], paint[i - 1][2]) + cost[i][0]
        paint[i][1] = min(paint[i - 1][0], paint[i - 1][2]) + cost[i][1]
        paint[i][2] = min(paint[i - 1][0], paint[i - 1][1]) + cost[i][2]

    # print(cost)
    # print(paint)
    return min(paint[-1])


if __name__ == "__main__":
    n = int(input())
    cost = []
    for i in range(n):
        c = list(map(int, input().split()))
        cost.append(c)
    
    result = dp(cost)
    print(result)