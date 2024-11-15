# 식료품 가게

import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
    t = int(input())
    for test_case in range(1, t + 1):
        n = int(input())
        prices = list(map(int, input().split()))
        
        q = deque()
        result = []
        for i in range(n * 2):
            if q and q[0] == prices[i]:
                tmp = q.popleft()
            else:
                result.append(prices[i])
                q.append(prices[i] * 4 // 3)
        print("#" + str(test_case), end=" ")
        print(*result)
