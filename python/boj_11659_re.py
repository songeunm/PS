# 구간 합 구하기 4
# 구간합

import sys
input = sys.stdin.readline

def prefixsum(nums):
    pfs = [0]
    for num in nums:
        pfs.append(pfs[-1] + num)
    return pfs

if __name__ == "__main__":
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    
    pfs = prefixsum(nums)
    for _ in range(m):
        i, j = map(int, input().split()) # 1 <= i, j, <= n
        answer = pfs[j] - pfs[i-1]
        print(answer)