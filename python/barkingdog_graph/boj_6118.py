# 숨바꼭질
# graph

import sys
from collections import deque
input = sys.stdin.readline

def bfs(g: list):
    s = 1
    q = deque([(s, 0)])
    vst = [0 for i in range(n+1)]
    vst[s] = 1

    max_value = 0
    barns = []
    
    while q:
        x, d = q.popleft()
        nd = d + 1
        for nx in g[x]:
            if vst[nx]:
                continue
            q.append((nx, nd))
            vst[nx] = 1
            if nd > max_value:
                barns = [nx]
                max_value = nd
            elif nd == max_value:
                barns.append(nx)
        # print(f"status of barns now: {barns}")
    return (barns, max_value)


if __name__ == "__main__":
    n, m = map(int, input().split())
    g = [ [] for i in range(n+1)]
    for i in range(m):
        a,b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)
    
    barns, max_value = bfs(g)
    print(min(barns), max_value, len(barns))