# 현재까지의 최솟값을 빠르게 구하기

import sys
import heapq

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    arr = []
    for _ in range(n):
        x = int(input())
        if x == 0:
            if arr:
                print(heapq.heappop(arr))
            else:
                print(0)
        else:
            heapq.heappush(arr, x)