# 1, 2, 3 더하기
# dp

import sys
input = sys.stdin.readline

def dp (n: int): # bottom-up
    if n == 1: # 1
        return 1
    elif n == 2: # 2 1+1
        return 2
    elif n == 3: # 3 2+1 1+2 1+1+1
        return 4
    
    lst = [0 for i in range(n + 1)]
    lst[1] = 1
    lst[2] = 2
    lst[3] = 4

    for x in range(4, n + 1):
        lst[x] = lst[x - 1] + lst[x - 2] + lst[x - 3]
    
    return lst[n]


if __name__ == "__main__":
    t = int(input())
    for tastcase in range(t):
        n = int(input())
        result = dp(n)
        print(result)