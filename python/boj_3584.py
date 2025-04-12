# 가장 가까운 공통 조상
# LCA

import sys
input = sys.stdin.readline

log = 20

def init(tree, root):
    n = len(tree)
    parent = [[0 for i in range(log)] for j in range(n)]
    depth = [0] * n
    
    # dfs
    st = [(root, 0)]
    visited = [0] * n
    visited[root] = 1
    while st:
        x, d = st.pop()
        for nx in tree[x]:
            if visited[nx]:
                continue
            st.append((nx, d+1))
            parent[nx][0] = x
            depth[nx] = d + 1
            visited[nx] = 1
    
    # binary lifting
    for k in range(1, log):
        for x in range(1, n):
            if parent[x][k-1] == 0:
                parent[x][k] = 0
            else:
                parent[x][k] = parent[ parent[x][k-1] ][k-1]
    return parent, depth

def lca(parent, depth, x, y):
    # 깊이 맞추기
    if depth[x] < depth[y]:
        x, y = y, x
    for k in reversed(range(log)):
        if depth[x] - (1 << k) >= depth[y]:
            x = parent[x][k]
    
    # lca 찾기
    if x == y:
        return x
    for k in reversed(range(log)):
        if parent[x][k] != parent[y][k]:
            x = parent[x][k]
            y = parent[y][k]
    return parent[x][0]

if __name__ == "__main__":
    testcase = int(input())
    for t in range(testcase):
        n = int(input())
        tree = [[] for _ in range(n+1)]
        root = {node for node in range(1, n+1)}
        for _ in range(n-1):
            a, b = map(int, input().split())
            tree[a].append(b)
            tree[b].append(a)
            if b in root:
                root.remove(b)
        
        parent, depth = init(tree, list(root)[0])
        x, y = map(int, input().split())
        answer = lca(parent, depth, x, y)
        print(answer)