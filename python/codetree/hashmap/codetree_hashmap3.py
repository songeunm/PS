# 문자열을 마치 Array의 Index 처럼 사용하기

import sys
from collections import defaultdict

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    d = defaultdict(int)
    for _ in range(n):
        string = input()
        d[string] += 1
    
    print(sorted(d.values())[-1])