# 중앙값

import sys
import heapq

input = sys.stdin.readline

if __name__ == "__main__":
    t = int(input())
    for testcase in range(t):
        m = int(input())
        seq = list(map(int, input().split()))
        upper = []
        lower = []
        median = seq[0]
        print(median, end=" ")
        for num in seq[1:]:
            if num >= median:
                heapq.heappush(upper, num)
            else:
                heapq.heappush(lower, -num)
            if (len(upper) + len(lower)) % 2 != 1:
                if len(upper) > len(lower):
                    heapq.heappush(lower, -median)
                    median = heapq.heappop(upper)
                elif len(upper) < len(lower):
                    heapq.heappush(upper, median)
                    median = - heapq.heappop(lower)
                print(median, end=" ")
        print()