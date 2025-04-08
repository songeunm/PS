# 배열 추출 2

import sys
import heapq

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    arr = []
    for _ in range(n):
        x = int(input())
        if x != 0:
            heapq.heappush(arr, (abs(x), x))
        else:
            if arr:
                abs_val, val = heapq.heappop(arr)
            else:
                val = 0
            print(val)