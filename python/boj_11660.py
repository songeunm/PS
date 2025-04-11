# 구간 합 구하기 5
# 누적합

import sys
input = sys.stdin.readline

def prefixsum(nums):
    n = len(nums)
    pfs = [[0]*(n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            pfs[i][j] = nums[i-1][j-1] + pfs[i-1][j] + pfs[i][j-1] - pfs[i-1][j-1]
            # print(*pfs, sep="\n")
            # print()
    return pfs

if __name__ == "__main__":
    n, m = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(n)]
    
    pfs = prefixsum(table)
    
    for _ in range(m):
        x1, y1, x2, y2 = map(int, input().split())
        answer = pfs[x2][y2] + pfs[x1-1][y1-1] - pfs[x2][y1-1] - pfs[x1-1][y2]
        print(answer)