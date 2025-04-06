# 가장 가까운 점

import sys
import heapq

input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())

    pq = []
    for _ in range(n):
        x, y = map(int, input().split())
        heapq.heappush(pq, (x+y, x, y))
    
    for _ in range(m):
        sum_xy, x, y = heapq.heappop(pq)
        x += 2
        y += 2
        heapq.heappush(pq, (x+y, x, y))
    
    _, x, y = heapq.heappop(pq)
    print(x, y)