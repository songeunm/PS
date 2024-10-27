# 구슬 찾기
# graph

import sys
input = sys.stdin.readline

def dfs(g: list):
    n = len(g)
    res = 0
    for s in range(1, n):
        st = [s]
        vst = [0 for node in range(n)]
        vst[s] = 1
        cnt = 0
        while st:
            x = st.pop()
            for nx in g[x]:
                if vst[nx]:
                    continue
                st.append(nx)
                vst[nx] = 1
                cnt += 1
        if cnt >= n//2:
            res += 1
    return res


if __name__ == "__main__":
    n, m = map(int, input().split())
    g_1 = [[] for node in range(n+1)]
    g_2 = [[] for node in range(n+1)]
    for compare in range(m):
        a, b = map(int, input().split())
        g_1[a].append(b) # 무거움 -> 가벼움
        g_2[b].append(a) # 가벼움 -> 무거움

    res_1 = dfs(g_1)
    res_2 = dfs(g_2)
    result = res_1 + res_2
    print(result)