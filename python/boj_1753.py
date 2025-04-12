# 최단경로

import sys
import heapq
input = sys.stdin.readline

def prim(graph, s):
    result = ["INF"] * len(graph)
    pq = [(0, s)]
    while pq:
        w, x = heapq.heappop(pq)
        if result[x] == "INF":
            result[x] = w
        else:
            continue
        for nx, nw in graph[x]:
            if result[nx] != "INF":
                continue
            heapq.heappush(pq, (w + nw, nx))
    return result

if __name__ == "__main__":
    v, e = map(int, input().split())
    k = int(input())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))

    answer = prim(graph, k)
    print(*answer[1:], sep="\n")