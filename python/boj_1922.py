# 네트워크 연결
# MST

import sys
input = sys.stdin.readline


### Kruskal
# union-find
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
    parent = [i for i in range(v+1)]
    graph.sort(key=lambda x: x[2])
    result = 0

    for a, b, weight in graph:
        if union(parent, a, b):
            result += weight
    return result


import heapq
from collections import defaultdict
### Prim
def prim(graph):
    v = len(graph)
    visited = [0 for _ in range(v+1)]
    pq = []

    # initial setting
    heapq.heappush(pq, (0, 1))
    result = 0

    # repitition
    while pq:
        weight, x = heapq.heappop(pq)

        if visited[x]:
            continue

        visited[x] = 1
        result += weight

        for nx, weight in graph[x]:
            if not visited[nx]:
                heapq.heappush(pq, (weight, nx))
    return result


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    graph_kruskal = []
    graph_prim = defaultdict(list)
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph_kruskal.append((a, b, c))
        graph_prim[a].append((b, c))
        graph_prim[b].append((a, c))

    answer_kruskal = kruskal(n, graph_kruskal)
    print(answer_kruskal)
    # answer_prim = prim(graph_prim)
    # print(answer_prim)