# 우주신과의 교감
# MST

import sys
import heapq
from time import sleep
input = sys.stdin.readline

def get_distance(u, v, nodes):
    x_calc = nodes[u][0] - nodes[v][0]
    y_calc = nodes[u][1] - nodes[v][1]
    return (x_calc**2 + y_calc**2)**0.5

def prim(nodes, edges):
    visited = [0 for _ in range(len(edges)+1)]
    pq = [(0, 1)]
    result = 0
    
    # for u in edges:
    #     for v in edges[v]:
    #         if visited[]:
    #             continue
    #         heapq.heappush(pq, (0, nx))
    
    while pq:
        w, x = heapq.heappop(pq)
        if visited[x]:
            continue
        visited[x] = 1
        result += w

        for nx in edges[x]:
            if visited[nx]:
                continue
            heapq.heappush(pq, (0, nx))

        for nx in nodes:
            if x == nx or visited[nx]:
                continue
            nw = get_distance(x, nx, nodes)
            heapq.heappush(pq, (nw, nx))
        # sleep(1)
        # print(x)
        # print(f"pq: {pq}")
        # print(f"visited: {visited}")
    return result

if __name__ == "__main__":
    n, m = map(int, input().split())
    nodes = {}
    for i in range(1, n+1):
        x, y = map(int, input().split())
        nodes[i] = (x, y)
    edges = {node: [] for node in range(1, n+1)}
    for _ in range(m):
        u, v = map(int, input().split())
        edges[u].append(v)
        edges[v].append(u)
    
    answer = prim(nodes, edges)
    print(f"{answer:.2f}")