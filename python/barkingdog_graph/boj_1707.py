# 이분 그래프
# graph

import sys
from collections import deque
input = sys.stdin.readline

def bfs(g: list):
    v = len(g)
    vst = [0 for node in range(len(g))]
    for s in range(1, v):
        if vst[s]:
            continue
        q = deque([s])
        vst[s] = 1
        while q:
            x = q.popleft()
            xg = vst[x]
            nxg = 1 if xg == 2 else 2
            for nx in g[x]:
                if vst[nx] == xg:
                    return False
                elif vst[nx]:
                    continue
                q.append(nx)
                vst[nx] = nxg
    return True


if __name__ == "__main__":
    K = int(input())
    for testcase in range(K):
        V, E = map(int, input().split())
        g = [ [] for node in range(V+1) ]
        for edge in range(E):
            u, v = map(int, input().split())
            g[u].append(v)
            g[v].append(u)
        
        
        result = bfs(g)
        if result:
            print("YES")
        else:
            print("NO")
