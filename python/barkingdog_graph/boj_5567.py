# 결혼식
# graph

import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    friends = {i:[] for i in range(1, n+1)}
    for i in range(m):
        a, b = map(int, input().split())
        friends[a].append(b)
        friends[b].append(a)
    
    q = deque([(1, 0)])
    attend = set()
    while q:
        x, i = q.popleft()
        if i >= 2:
            continue
        for nx in friends[x]:
            q.append((nx, i+1))
            attend.add(nx)
    
    answer = len(attend)-1 if len(attend)-1 > 0 else 0
    print(answer)