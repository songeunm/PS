# 대응되는 수와 문자

import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())

    d = {}
    for i in range(1, n+1):
        string = input().rstrip()
        d[string] = str(i)
        d[str(i)] = string
    
    for i in range(m):
        find = input().rstrip()
        print(d[find])