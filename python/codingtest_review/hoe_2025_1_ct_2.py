import math
import time

# 기존 방법

import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
    n, k, p = map(int, input().split())
    g = [list(map(int, input().split())) for i in range(n)]
    b = list(map(int, input().split()))

    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    def get_point(sx, sy, kw):
        q = deque([(sx, sy, 1)])
        vst = [[0 for i in range(n)] for j in range(n)]
        vst[sx][sy] = 1
        point = g[sx][sy]
        while q:
            x, y, w = q.popleft()
            if w >= kw:
                continue
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if nx<0 or ny<0 or nx>=n or ny>=n:
                    continue
                if vst[nx][ny]:
                    continue
                vst[nx][ny] = 1
                point += g[nx][ny]
                q.append((nx, ny, w + 1))
        return point
    
    def search_comb(ki=0, power=0, points=0, result=float('inf')):
        if points == p:
            if power < result:
                result = power
            return result
        if ki >= k:
            return result
        for i in range(n):
            for j in range(n):
                now_point = get_point(i, j, ki + 1)
                if points + now_point <= p:
                    for nki in range(ki + 1, k + 1):
                        power += b[ki]
                        points += now_point
                        result = search_comb(nki, power, points, result)
                        power -= b[ki]
                        points -= now_point
        return result
    
    start = time.time()
    result = search_comb()
    if result == float('inf'):
        print(-1)
    else:
        print(result)
    end = time.time()
    print(end-start)

# 0.0005