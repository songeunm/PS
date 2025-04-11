# 나머지 합
# 누적합

import sys
input = sys.stdin.readline

def prefixsum(nums, m):
    pfs = [0]
    result = [0 for i in range(m)]
    result[0] += 1
    for num in nums:
        calc = (pfs[-1] + num) % m
        pfs.append(calc)
        result[calc] += 1
    return result

if __name__ == "__main__":
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    
    calc = prefixsum(nums, m)
    answer = 0
    for i in range(m):
        answer += calc[i]*(calc[i]-1)//2
    print(answer)