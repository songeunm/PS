# 케빈 베이컨의 6단계 법칙
# graph

import sys
import pprint
input = sys.stdin.readline

def fw(g: list):
    n = len(g)
    for k in range(n):
        for u in range(n):
            for v in range(n):
                g[u][v] = min(g[u][v], g[u][k]+g[k][v])

if __name__ == "__main__":
    n, m = map(int, input().split())
    g = [ [float('inf') for i in range(n+1)] for ㅓ in range(n+1) ]
    for i in range(m):
        a, b = map(int, input().split())
        g[a][b] = 1
        g[b][a] = 1
    
    # pprint.pprint(g)
    fw(g)
    # pprint.pprint(g)

    min_value = float('inf')
    res = 0
    for i in range(1,n+1):
        tmp = 0
        for j in range(1,n+1):
            if i == j:
                continue
            tmp += g[i][j]
        if tmp < min_value:
            min_value = tmp
            res = i
    print(res)
