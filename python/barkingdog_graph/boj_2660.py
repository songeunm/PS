# 회장뽑기 
# graph


### floyd-warshall
import sys
import pprint
input = sys.stdin.readline

def fw(g: list):
    n = len(g)
    for k in range(n):
        for a in range(n):
            for b in range(a+1, n):
                g[a][b] = min(g[a][b], g[a][k]+g[k][b])
                g[b][a] = g[a][b]

if __name__ == "__main__":
    n = int(input())
    g = [ [float('inf') for i in range(n+1)] for j in range(n+1)]
    while 1:
        u, v = map(int, input().split())
        if u == -1 and v == -1:
            break
        g[u][v] = 1
        g[v][u] = 1
    
    # pprint.pprint(g)
    fw(g)
    # pprint.pprint(g)

    min_val = float('inf')
    res = []
    for i in range(1, n+1):
        g[i][i] = 0
        tmp = max(g[i][1:])
        if tmp < min_val:
            min_val = tmp
            res = [i]
        elif tmp == min_val:
            res.append(i)
    
    print(min_val, len(res))
    print(*sorted(res))

### bfs
import sys
import pprint
from collections import deque
input = sys.stdin.readline

def bfs(g: list, s: int):
    res = 0
    q = deque([(s, res)])
    n = len(g)
    vst = {node: 0 for node in range(1, n+1)}
    vst[s] = 1

    while q:
        x, d = q.popleft()
        for n in g[x]:
            if vst[n]:
                continue
            q.append((n, d+1))
            if res < d+1:
                res = d+1
            vst[n] = 1
    return res
    

if __name__ == "__main__":
    n = int(input())
    g = {node: [] for node in range(1, n+1)}
    while 1:
        u, v = map(int, input().split())
        if u == -1 and v == -1:
            break
        g[u].append(v)
        g[v].append(u)
    
    min_val = float('inf')
    res = []
    for i in range(1, n+1):
        tmp = bfs(g, i)
        if tmp < min_val:
            min_val = tmp
            res = [i]
        elif tmp == min_val:
            res.append(i)
    
    print(min_val, len(res))
    print(*sorted(res))