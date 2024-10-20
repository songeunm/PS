# 환승
# graph

import sys
from collections import deque
input = sys.stdin.readline

def bfs(g: list, n: int, m: int):
    if n == 1:
        return 1
    s = 1
    q = deque([(s, 1)])
    vst = [0 for i in range(n + m + 1)]
    vst[s] = 1

    while q:
        x, d = q.popleft()
        nd = d + 1
        for nx in g[x]:
            if vst[nx]:
                continue
            if nx == n:
                return nd
            q.append((nx, nd))
            vst[nx] = 1
        # print(f"status of q now: {q}")
    
    return -1

if __name__ == "__main__":
    n, k, m = map(int, input().split())
    g = [ set() for i in range(n+1+m) ]
    for ht in range(1, m+1):
        stations = list(map(int, input().split()))
        g[n + ht].update(stations)
        for s in stations:
            g[s].add(n + ht)
    
    res_bfs = bfs(g, n, m)
    if res_bfs < 0:
        print(res_bfs)
    else:
        result = res_bfs // 2 + 1
        print(result)