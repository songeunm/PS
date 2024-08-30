"""
소가 길을 건너간 이유 6
bfs
"""

import sys
from pprint import pprint
from collections import deque
from itertools import combinations

input = sys.stdin.readline

def bfs(sx: int, sy: int, Map:list, visit: list):
    q = deque([(sx, sy)])
    visit[sx][sy] = 1
    n = len(visit)
    count = 0

    dir_x = [ 0,-1, 0, 1]
    dir_y = [-1, 0, 1, 0]

    while q:
        x, y = q.popleft()
        if Map[x][y] == 2: # cow
            count += 1
        for i in range(4):
            nx = x + dir_x[i]
            ny = y + dir_y[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if Map[nx][ny] == 1: # road
                continue
            nx += dir_x[i]
            ny += dir_y[i]
            if not visit[nx][ny]:
                q.append((nx, ny))
                visit[nx][ny] = 1
    return count

def cows(Map: list, N: int):
    visit = [[0 for i in range(N*2-1)] for j in range(N*2-1)]
    cow_group = []

    for i in range(0, N*2-1, 2):
        for j in range(0, N*2-1, 2):
            if visit[i][j] == 0:
                cow_group.append( bfs(i, j, Map, visit) )
    #print("visit:")
    #pprint(visit)
    #print(f"cow_group: {cow_group}")
    
    res = 0
    for group1, group2 in combinations(cow_group, 2):
        res += group1 * group2
    return res

if __name__ == "__main__":
    N, K, R = map(int, input().split())
    Map = [[0 for i in range(N*2-1)] for j in range(N*2-1)]
    for r in range(R):
        r1, c1, r2, c2 = map(lambda x: (x-1)*2, map(int, input().split()))
        Map[(r1+r2)//2][(c1+c2)//2] = 1
        
    for k in range(K):
        r, c = map(lambda x: (x-1)*2, map(int, input().split()))
        Map[r][c] = 2

    print( cows(Map, N) )