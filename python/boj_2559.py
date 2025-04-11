# 수열
# 구간합

import sys
input = sys.stdin.readline

def prefixsum(nums):
    pfs = [0]
    for num in nums:
        pfs.append(pfs[-1] + num)
    return pfs

if __name__ == "__main__":
    n, k = map(int, input().split())
    temp = list(map(int, input().split()))
    
    pfs = prefixsum(temp)
    answer = float('-inf')
    for i in range(k, n+1):
        answer = max(answer, pfs[i] - pfs[i-k])
    print(answer)