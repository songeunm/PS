# 효율적인 해킹
# graph

import sys
input = sys.stdin.readline

def dfs(g: dict):
    st = []
    n = len(g)
    max_value = 0
    res = []
    for s in range(1, n+1):
        st.append(s)
        vst = [0 for i in range(n+1)]
        vst[s] = 1
        tmp = 0
        while st:
            x = st.pop()
            for u in g[x]:
                if vst[u]:
                    continue
                st.append(u)
                vst[u] = 1
                tmp += 1
        if tmp > max_value:
            max_value = tmp
            res = [s]
        elif tmp == max_value:
            res.append(s)
    return res


if __name__ == "__main__":
    n, m = map(int, input().split())
    g = {node: [] for node in range(1, n+1)}
    for i in range(m):
        a, b = map(int, input().split())
        g[b].append(a)

    result = dfs(g)
    print(*result)