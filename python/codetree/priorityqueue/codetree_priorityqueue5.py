# 배열 추출

import sys
import heapq

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    pq = []
    for _ in range(n):
        x = int(input())
        if x > 0:
            heapq.heappush(pq, -x)
        elif x == 0:
            if pq:
                print(-heapq.heappop(pq))
            else:
                print(0)