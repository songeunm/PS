# 앞에서부터 삭제하기 2

import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    
    cumulative_sum = nums[-1]
    min_value = nums[-1]
    length = 0
    answer = float('-inf')
    for i in range(n-2, 0, -1):
        cumulative_sum += nums[i]
        min_value = min(min_value, nums[i])
        length += 1
        result = (cumulative_sum - min_value) / length
        if answer < result:
            answer = result
    
    print(f"{answer:.2f}")