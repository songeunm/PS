# 현재까지의 최댓값을 빠르게 구하기

import sys
import heapq

input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    nums = list(map(lambda x: -int(x), input().split()))

    heapq.heapify(nums)
    for _ in range(m):
        num = - heapq.heappop(nums)
        heapq.heappush(nums, -(num - 1))
    answer = - heapq.heappop(nums)
    print(answer)