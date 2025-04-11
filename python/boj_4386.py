# 별자리 만들기
# MST

import sys
from collections import defaultdict
import heapq
input = sys.stdin.readline

def prim(graph):
    pq = [(0, 0)]
    visited = [0 for _ in range(len(graph))]
    result = 0
    
    while pq:
        weight, x = heapq.heappop(pq)
        if visited[x]:
            continue
        visited[x] = 1
        result += weight
        
        for nx, w in graph[x]:
            if not visited[nx]:
                heapq.heappush(pq, (w, nx))
    return result


if __name__ == "__main__":
    n = int(input())
    star = []
    for _ in range(n):
        x, y = map(float, input().split())
        star.append((x, y))
    
    graph = defaultdict(list)
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            ax, ay = star[i][0], star[i][1]
            bx, by = star[j][0], star[j][1]
            distance = ((ax-bx)**2 + (ay-by)**2)**0.5
            graph[i].append((j, distance))
            graph[j].append((i, distance))
    
    answer = prim(graph)
    print(answer)