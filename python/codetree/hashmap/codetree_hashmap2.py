# 아주 큰 숫자를 Array의 Index로 사용하기

import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    n_seq = list(map(int, input().split()))
    m_num = list(map(int, input().split()))

    d = {}
    for s in n_seq:
        try:
            d[s] += 1
        except:
            d[s] = 1
    
    for n in m_num:
        try:
            print(d[n], end=" ")
        except:
            print(0, end=" ")