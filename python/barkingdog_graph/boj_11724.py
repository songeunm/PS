# 연결 요소의 개수
# graph

import sys
input = sys.stdin.readline

def dfs(g: dict, vst: dict, s: int):
    st = [s]
    vst[s] = 1

    while st:
        x = st.pop()
        for n in g[x]:
            if vst[n]:
                continue
            st.append(n)
            vst[n] = 1

if __name__ == "__main__":
    n, m = map(int, input().split())
    g = {node: [] for node in range(1, n+1)}

    for i in range(m):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)
    
    vst = {node: 0 for node in range(1, n+1)}
    cnt = 0
    for s, v in vst.items():
        if not v:
            dfs(g, vst, s)
            cnt += 1
    
    print(cnt)