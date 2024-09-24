# 비밀번호 찾기
# hash

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())

    d = {}
    for i in range(n):
        url, pw = input().split()
        d[url] = pw
    
    for i in range(m):
        search_url = input().rstrip()
        print(d[search_url])
