# DFS와 BFS 
# graph

import sys
from collections import deque
input = sys.stdin.readline

def bfs(s: int, g: dict):
    q = deque([s])
    vst = {node: 0 for node in range(1, len(g)+1)}
    vst[s] = 1
    res = []
    while q:
        x = q.popleft()
        res.append(x)
        n_lst = sorted(g[x])
        for n in n_lst:
            if vst[n]:
                continue
            q.append(n)
            vst[n] = 1
    return res

def dfs(s: int, g: dict):
    st = [s]
    vst = {node: 0 for node in range(1, len(g)+1)}
    vst[s] = 1
    res = [s]
    while st:
        x = st.pop()
        if not vst[x]:
            vst[x] = 1
            res.append(x)
        n_lst = sorted(g[x], reverse=True)
        # print(f"x={x}: {n_lst}")
        for n in n_lst:
            if vst[n]:
                continue
            st.append(n)
        # print(st)
    return res

def dfs_recursive(x: int, g: dict, vst: dict, res: list):
    res.append(x)
    vst[x] = 1
    n_lst = sorted(g[x])
    for n in n_lst:
        if not vst[n]:
            dfs_recursive(n, g, vst, res)



if __name__ == "__main__":
    n, m, v = map(int, input().split())
    g = {node: [] for node in range(1, n+1)}

    for i in range(m):
        x, y = map(int, input().split())
        g[x].append(y)
        g[y].append(x)

    # res = []
    # vst = {node: 0 for node in range(1, len(g)+1)}
    # dfs_recursive(v, g, vst, res)
    # print( *res )

    print( *dfs(v, g) )
    print( *bfs(v, g) )