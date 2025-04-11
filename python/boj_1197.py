# 최소 스패닝 트리
# MST

import sys
input = sys.stdin.readline

# union-find (non-recursion)
def find(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(parent, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)
    if x_root == y_root:
        return False
    parent[y_root] = x_root
    return True

# kruskal
def kruskal(v, graph):
    graph.sort(key=lambda x: x[2])
    parent = [i for i in range(v+1)]
    result = 0

    for a, b, c in graph:
        if union(parent, a, b):
            result += c
    return result

if __name__ == "__main__":
    v, e = map(int, input().split())
    graph = []
    for _ in range(e):
        a, b, c = map(int, input().split())
        graph.append((a, b, c))
    
    answer = kruskal(v, graph)
    print(answer)