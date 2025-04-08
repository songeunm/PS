# 정원 입장은 선착순

import sys
import heapq

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    time = 0
    pq = []
    for i in range(1, n+1):
        a, t = map(int, input().split())
        heapq.heappush(pq, (a, i, t))

    line = []
    time = 0
    answer = 0
    while pq or line:
        if pq:
            # print(pq)
            while pq and time >= pq[0][0]:
                a, i, t = heapq.heappop(pq)
                heapq.heappush(line, (i, a, t))
            if not line:
                a, i, t = heapq.heappop(pq)
                heapq.heappush(line, (i, a, t))
        if line:
            # print(line)
            i, a, t = heapq.heappop(line)
            wait = time - a if time > a else 0
            answer = wait if wait > answer else answer
            if time < a:
                time = a + t
            else:
                time = time + t
            # print(i, time, a, t, wait)
    print(answer)