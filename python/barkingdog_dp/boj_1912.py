# 연속합
# dp

import sys
input = sys.stdin.readline

def dp(nums: list):
    n = len(nums)
    memo = [0 for i in range(n)]
    memo[0] = nums[0]
    sum = max(nums[0], 0)

    for i in range(1, n):
        sum += nums[i]
        memo[i] = max(memo[i - 1], sum)
        if sum < 0:
            sum = 0
    # print(memo)
    return memo[-1]

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    result = dp(nums)
    print(result)