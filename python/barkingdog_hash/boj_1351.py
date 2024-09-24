# 무한 수열
# hash DP

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, p, q = map(int, input().split())

    d = {0: 1}
    st = [n]
    while not d.get(n, 0):
        i = st.pop()
        if not d.get(i//p, 0):
            st.append(i)
            st.append(i//p)
        elif not d.get(i//q, 0):
            st.append(i)
            st.append(i//q)
        else:
            d[i] = d[i//p] + d[i//q]
        
    print(d[n])
