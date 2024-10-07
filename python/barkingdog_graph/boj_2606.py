# 바이러스 
# graph

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    g = {node: [] for node in range(1, n+1)}
    m = int(input())
    for i in range(m):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)
    
    # dfs
    st = [1]
    vst = [0 for i in range(n+1)]
    vst[1] = 1
    cnt = 0
    while st:
        x = st.pop()
        for n in g[x]:
            if vst[n]:
                continue
            st.append(n)
            vst[n] = 1
            cnt += 1

    print(cnt)