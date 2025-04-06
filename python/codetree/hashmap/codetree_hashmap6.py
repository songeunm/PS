# 세 수의 합

import sys
from collections import defaultdict

input = sys.stdin.readline

def sum_of_three_numbers(nums, k):
    n = len(nums)
    result = 0
    cnt = defaultdict(int)
    for i in range(n):
        calc = k - nums[i]
        if calc in cnt:
            result += cnt[calc]
        for j in range(i):
            pair_sum = nums[i] + nums[j]
            cnt[pair_sum] += 1
    return result

if __name__ == "__main__":
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    
    answer = sum_of_three_numbers(nums, k)
    print(answer)