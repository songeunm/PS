# Hanyang Popularity Exceeding Competition

import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    x = 0
    for _ in range(n):
        p,c = map(int, input().split())
        if abs(p - x) <= c:
            x += 1
    print(x)