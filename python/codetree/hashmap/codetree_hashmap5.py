# 두 수의 합

import sys
from collections import defaultdict

input = sys.stdin.readline

def sum_of_two_numbers(nums, nums_dict, target):
    cnt = 0
    r_nums = list(map(lambda x: target - x, nums))
    for num in r_nums:
        if num in nums_cnt:
            if target == 2 * num:
                cnt -= 1
            cnt += nums_cnt[num]
    return cnt//2

if __name__ == "__main__":
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    nums_cnt = defaultdict(int)
    for num in nums:
        nums_cnt[num] += 1

    result = sum_of_two_numbers(nums, nums_cnt, k)
    print(result)