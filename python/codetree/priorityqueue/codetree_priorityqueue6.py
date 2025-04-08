# 마지막으로 남은 숫자

import sys
import heapq

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    nums = list(map(lambda x: -int(x), input().split()))
    heapq.heapify(nums)
    while len(nums) >= 2:
        x = - heapq.heappop(nums)
        y = - heapq.heappop(nums)
        if x != y:
            heapq.heappush(nums, - abs(x-y))
    if nums:
        answer = - nums[0]
    else:
        answer = -1
    print(answer)