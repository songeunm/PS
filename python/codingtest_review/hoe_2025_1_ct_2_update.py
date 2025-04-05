# 최적화 방안
# 1. 화살을 소요 힘 순 오름차순으로 정렬하여 첫번째 조건 부합 조합을 찾을 경우 최소 힘 소요가 되도록 함
# 2. memoization을 통해 중복되는 값의 재사용하여 조합의 경우의 수를 줄이도록 함
#    -> get_point를 통해 모든 경우의 점수를 구하는 과정과 조합을 구하는 과정을 분리

import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
    n, k, p = map(int, input().split())
    g = [list(map(int, input().split())) for i in range(n)]
    b = list(map(int, input().split()))
    # 소요되는 힘을 정렬된 상태로 접근
    b = sorted([(i+1, b[i]) for i in range(len(b))], key=lambda x: b[1])

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

    def get_all_possible_points(ki=0):
        memo = set()
        if ki >= k:
            return result
        for i in range(n):
            for j in range(n):
                now_point = get_point(i, j, b[ki][0])
                memo.add(now_point)
        return memo
    
    def search_comb(ki=0, power=0, points=0, result=float('inf')):
        memo = []
        if points == p:
            if power < result:
                result = power
            return result
        if ki >= k:
            return result
        possible_points = get_all_possible_points(ki)
        for pp in possible_points:
            if points + pp <= p:
                for nki in range(ki + 1, k + 1):
                    power += b[ki][1]
                    points += pp
                    result = search_comb(nki, power, points, result)
                    power -= b[ki][1]
                    points -= pp
        return result
    
    start = time.time()
    result = search_comb()
    if result == float('inf'):
        print(-1)
    else:
        print(result)
    end = time.time()
    print(end-start)

# 0.0002