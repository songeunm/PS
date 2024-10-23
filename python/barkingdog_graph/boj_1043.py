# 거짓말
# graph

import sys
from collections import deque
input = sys.stdin.readline

def bfs(g: list, s: list, n: int, m: int):
    vst = [0 for node in range(len(g))]
    res = 0
    for sx in s:
        q = deque([sx])
        vst[sx] = 1
        while q:
            x = q.popleft()
            for nx in g[x]:
                if vst[nx]:
                    continue
                q.append(nx)
                vst[nx] = 1
                if nx >= n+1:
                    res += 1
    return m-res

if __name__ == "__main__":
    n, m = map(int, input().split())
    g = [[] for node in range(n + m + 1)]
    t = list(map(int, input().split()))
    t = t[1:]
    for party in range(n+1, n+1+m):
        people = list(map(int, input().split()))
        people = people[1:]
        for p in people:
            g[p].append(party)
            g[party].append(p)

    result = bfs(g, t, n, m)
    print(result)