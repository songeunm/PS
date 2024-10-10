# 경로 찾기
# graph

import sys
input = sys.stdin.readline

def fw(g):
    l = len(g)
    for i in range(l):
        # print(i)
        for x in range(l):
            for y in range(l):
                g[x][y] = (g[x][y]) or (g[x][i] and g[i][y])
        # print(g)


if __name__ == "__main__":
    n = int(input())
    g = [list(map(int, input().split())) for i in range(n)]

    fw(g)
    for res in g:
        print(*res)