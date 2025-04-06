# 정수 명령 처리 6

import sys
import heapq

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    pq = []
    for _ in range(n):
        cmd = input().split()
        if cmd[0] == "push":
            heapq.heappush(pq, -int(cmd[1]))
        elif cmd[0] == "pop":
            print(-heapq.heappop(pq))
        elif cmd[0] == "size":
            print(len(pq))
        elif cmd[0] == "empty":
            if len(pq) == 0:
                print(1)
            else:
                print(0)
        else:
            print(-pq[0])