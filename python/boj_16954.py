# 우ㅁ직이는 미로 탈출
# BFS

import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 0, 1, -1, 0, 1]

def move_walls(grid):
    row = [(-1, ".") for _ in range(8)]
    for i in range(8):
        for j, row_info in enumerate(row):
            r, w = row_info
            row[j] = (r+1, grid[i][j])
            grid[i][j] = w
    # print(*grid, sep="\n")

def move_character(grid, q):
    # print(*grid, sep="\n")
    next_q = []
    visited = set()
    while q:
        x, y = q.popleft()
        if grid[x][y] == "#":
            # print("벽과 부딪침")
            continue
        if (x, y) == (0, 7):
            # print("도착")
            return False, []
        for d in range(9):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < 8 and 0 <= ny < 8:
                if grid[nx][ny] == "#":
                    # print("벽이라 갈 수 없음")
                    continue
                if (nx, ny) in visited:
                    # print("이미 방문하기로한 칸")
                    continue
                next_q.append((nx, ny))
                visited.add((nx, ny))
                # print("방문 완료")
    move_walls(grid)
    # print(next_q)
    return True, next_q

if __name__ == "__main__":
    grid = [list(input().rstrip()) for _ in range(8)]
    x, y = 7, 0 #from / to = 0, 7
    
    next = True
    next_q = (x, y)
    q = deque([next_q])
    
    while next and next_q:
        next, next_q = move_character(grid, q)
        q.extend(next_q)
    if next:
        print(0)
    else:
        print(1)