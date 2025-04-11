# LCA

import sys
input = sys.stdin.readline

log = 20

def dfs(tree):
    n = len(tree)
    parent = [[-1 for i in range(log)] for j in range(n)]
    depth = [0 for _ in range(n)]
    
    # dfs
    st = [(1, 0)]
    visited = [0 for _ in range(n)]
    visited[1] = 1
    while st:
        x, d = st.pop()
        for nx in tree[x]:
            if visited[nx]:
                continue
            st.append((nx, d + 1))
            parent[nx][0] = x
            depth[nx] = d + 1
            visited[nx] = 1
    
    # binary lifting
    for k in range(1, log):
        for x in range(1, n):
            if parent[x][k-1] == -1:
                parent[x][k] = -1
            else:
                parent[x][k] = parent[parent[x][k-1]][k-1]
    return parent, depth

def lca(x, y, parent, depth):
    # 깊이 맞추기
    if depth[x] < depth[y]:
        x, y = y, x
    for k in reversed(range(log)):
        # 1 << k 는 비트이동을 통한 2**k 표현 (더 빠르다)
        if depth[x] - (1 << k) >= depth[y]:
            x = parent[x][k]
    
    # LCA 구하기
    if x == y:
        return x
    for k in reversed(range(log)):
        if parent[x][k] != parent[y][k]:
            x = parent[x][k]
            y = parent[y][k]
    return parent[x][0]

if __name__ == "__main__":
    n = int(input())
    tree = [[] for _ in range(n+1)]
    for _ in range(n-1):
        x, y = map(int, input().split())
        tree[x].append(y)
        tree[y].append(x)
    
    # 전처리
    parent, depth = dfs(tree)
    
    m = int(input())
    for _ in range(m):
        x, y = map(int, input().split())
        answer = lca(x, y, parent, depth)
        print(answer)