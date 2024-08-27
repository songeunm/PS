import sys
from collections import deque
from pprint import pprint

input = sys.stdin.readline

# bfs

def walls (location: int):
    result = []
    if location&0b0001 == 2**0: # The west
        result.append(False) # Wall
    else:
        result.append(True) # No wall
    if location&0b0010 == 2**1: # The north
        result.append(False) # Wall
    else:
        result.append(True) # No wall
    if location&0b0100 == 2**2: # The east
        result.append(False) # Wall
    else:
        result.append(True) # No wall
    if location&0b1000 == 2**3: # The south
        result.append(False) # Wall
    else:
        result.append(True) # No wall
    return result

def bfs (Map: list, visit: list, sx: int, sy: int, room_number: int):
    q = deque([(sx, sy)])
    visit[sx][sy] = room_number
    size = 1
    over_the_wall = []

    dir_x = [ 0,-1, 0, 1]
    dir_y = [-1, 0, 1, 0]

    while q:
        x, y = q.popleft()
        for i, go in enumerate(walls(Map[x][y])):
            nx = x + dir_x[i]
            ny = y + dir_y[i]
            if nx<0 or ny<0 or nx>=len(Map) or ny>=len(Map[0]):
                continue
            if go != True:
                over_the_wall.append((nx, ny))
                continue
            if not visit[nx][ny]:
                q.append((nx, ny))
                visit[nx][ny] = room_number
                size += 1
    return size, over_the_wall

def castle (Map: list, visit: list, N: int, M: int):
    room_number = 1
    room_size = {}
    sx, sy = 0, 0
    q = deque([(0, sx, sy)])
    max_size = 0
    max_sum_size = 0

    while q:
        conn_size, x, y = q.popleft()
        if visit[x][y]:
            continue
        size, otw = bfs(Map, visit, x, y, room_number)
        room_size[room_number] = size
        max_size = max(max_size, size)
        max_sum_size = max(max_sum_size, size+conn_size)
#        print(f"room_number{room_number}, size: {size}, max size: {max_sum_size}")
#        pprint(visit)
        for px, py in otw:
            if visit[px][py] == room_number:
                continue
            elif visit[px][py] == 0:
                q.append((size, px, py))
            else:
                max_sum_size = max(max_sum_size, size+room_size[visit[px][py]])
        room_number += 1
    
    print(room_number-1)
    print(max_size)
    print(max_sum_size)


if __name__ == "__main__":
    N, M = map(int, input().split())
    Map = [list(map(int, input().split())) for _ in range(M)]
    visit = [[0 for i in range(N)] for j in range(M)]

    castle(Map, visit, N, M)