# 문자열 지옥에 빠진 호석
# hash, dfs

import sys
from collections import deque
input = sys.stdin.readline

def calc(x, y, n, m):
    nx, ny = 0, 0
    if x < 0:
        nx = x + n
    elif x >= n:
        nx = x - n
    else:
        nx = x
    if y < 0:
        ny = y + m
    elif y >= m:
        ny = y - m
    else:
        ny = y
    return nx, ny

def dfs(sx: int, sy: int, target:str, w: list):
    i = 0
    q = deque([(sx, sy, i)])
    dir_x = [-1,  0,  1, -1, 1, -1, 0, 1]
    dir_y = [-1, -1, -1,  0, 0,  1, 1, 1]
    count = 0
    # print(f"target: {target}")

    while q:
        x, y, i = q.pop()
        # print(f"{i}: ({x}, {y})")
        if i >= len(target)-1:
            count += 1
            continue
        for d in range(8):
            nx = x + dir_x[d]
            ny = y + dir_y[d]
            nx, ny = calc(nx, ny, n, m)
            if w[nx][ny] == target[i+1]:
                q.append((nx, ny, i+1))
        # print(q)
    return count

if __name__ == "__main__":
    n, m, k = map(int, input().split())
    world = [list(input().rstrip()) for i in range(n)]
    targets = [input().rstrip() for i in range(k)]

    memo = {} # memoization 도입
    for t in targets:
        if memo.get(t, 0):
            print(memo[t])
        else:
            count = 0
            for i in range(n):
                for j in range(m):
                    if  world[i][j] == t[0]:
                        count += dfs(i, j, t, world)
            memo[t] = count
            print(count)