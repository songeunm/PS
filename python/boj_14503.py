# 로봇 청소기
# gold 5
# 구현, 시뮬레이션

import sys

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def robot_vacuum(r: int, c: int, d: int, g: list):
    """
    args:
        r: 로봇 청소기의 위치 행
        c: 로봇 청소기의 위치 열
        d: 로봇 청소기의 방향
        g: 방의 구조
    returns:
        로봇 청소기가 청소한 칸의 수
    """
    n = len(g)
    m = len(g[0])
    cleaned = [[0 for i in range(m)] for j in range(n)]
    cnt = 0
    x, y = r, c
    while 1:
        if not cleaned[x][y]:
            # print("clean the place")
            cleaned[x][y] = 1
            cnt += 1
        else:
            around = [0, 0, 0, 0]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if g[nx][ny]:
                    around[i] = -1
                elif cleaned[nx][ny]:
                    around[i] = 1
            if 0 in around:
                # print("turn")
                d = d - 1 if d - 1 >= 0 else d - 1 + 4
                nx = x + dx[d]
                ny = y + dy[d]
                if (not g[nx][ny]) and (not cleaned[nx][ny]):
                    x = nx
                    y = ny
            else:
                nx = x - dx[d]
                ny = y - dy[d]
                if g[nx][ny] == 0:
                    # print("back")
                    x = nx
                    y = ny
                else:
                    # print("quit")
                    return cnt
        # print("---")
        # print("g")
        # print(*g, sep='\n')
        # print(f"cleaned {x} {y} {d}")
        # print(*cleaned, sep='\n')

if __name__ == "__main__":
    n, m = map(int, input().split()) # 3 <= n, m <= 50
    r, c, d = map(int, input().split()) # N: 0, E: 1, S: 2, W: 3
    g = [list(map(int, input().split())) for i in range(n)]
    # print(*g, sep='\n') # test print
    
    result = robot_vacuum(r, c, d, g)
    print(result)




# -----------------------------------------------------------------
# GPT 개선포인트 수정
# 1. around 배열 대신 has_dirty 플래그 사용
# 2. 방향 회전 함수 분리
# 3. 명확한 변수명
# 4. 명확한 while 종료 조건

import sys

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left(d):
    return (d + 3) % 4

def robot_vacuum(r: int, c: int, d: int, room: list):
    """
    args:
        r: 로봇 청소기의 위치 행
        c: 로봇 청소기의 위치 열
        d: 로봇 청소기의 방향
        room: 방의 구조
    returns:
        로봇 청소기가 청소한 칸의 수
    """
    n = len(room)
    m = len(room[0])
    cleaned = [[0 for i in range(m)] for j in range(n)]
    cnt = 0
    x, y = r, c
    while 1:
        if not cleaned[x][y]:
            cleaned[x][y] = 1
            cnt += 1
        else:
            has_dirty = False
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if room[nx][ny] == 0 and cleaned[nx][ny] == 0:
                    has_dirty = True
                    break
            if has_dirty:
                d = turn_left(d)
                nx = x + dx[d]
                ny = y + dy[d]
                if (not room[nx][ny]) and (not cleaned[nx][ny]):
                    x = nx
                    y = ny
            else:
                nx = x - dx[d]
                ny = y - dy[d]
                if room[nx][ny] == 0:
                    x = nx
                    y = ny
                else:
                    return cnt

if __name__ == "__main__":
    n, m = map(int, input().split()) # 3 <= n, m <= 50
    r, c, d = map(int, input().split()) # N: 0, E: 1, S: 2, W: 3
    room = [list(map(int, input().split())) for i in range(n)]
    
    result = robot_vacuum(r, c, d, room)
    print(result)
