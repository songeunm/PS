# 경로 찾기
# graph

import sys
input = sys.stdin.readline

def dfs(s: int, g: list, check: list, res: list):
    st = [s]
    conn = {s}

    while st:
        x = st.pop()
        print(f"x: {x}")
        check[x] = 1
        for i, n in enumerate(g[x]):
            print(f"n: {i} {n}")
            if not n:
                continue
            if i == s:
                res[i][i] = 1
                continue
            print(f"pushed")
            st.append(i)
            for c in conn:
                res[c][i] = 1
            conn.add(i)
        print(f"st: {st}")
        print(f"conn: {conn}")
        print(f"res: {res}")


if __name__ == "__main__":
    n = int(input())
    g = [list(map(int, input().split())) for i in range(n)]

    res = [[0 for i in range(n)] for j in range(n)]
    check = [0 for i in range(n)]

    for i in range(n):
        if not check[i]:
            print(f"--- start dfs with {i}")
            dfs(i, g, check, res)