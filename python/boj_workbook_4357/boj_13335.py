"""
트럭
구현, 자료구조, 시뮬레이션, 큐
"""

import sys
from collections import deque
from time import sleep

input = sys.stdin.readline

def cross_bridge(w: int, L: int, trucks: list):
    q = deque([])

    time = 0
    i = 0
    n = len(trucks)
    locations = [0 for _ in range(n)]
    weight = 0
    done = False

    while not done:
        # 큐의 트럭 이동
        for _ in range(len(q)):
            idx = q.popleft()
            locations[idx] += 1
            if locations[idx] > w:
                weight -= trucks[idx]
                if idx == n-1:
                    done = True
            else:
                q.append(idx)

        # 제한 하중을 넘지 않고, 다리가 꽉 차지 않은 경우 다음 트럭 출발
        if i < n:
            if weight+trucks[i] <= L and len(q) < w:
                q.append(i)
                locations[i] += 1
                weight += trucks[i]
#                print(f"{i}번째 트럭 출발!")
                i += 1

#        print(f"time {time}: {locations}, weight: {weight}")
#        sleep(0.1)
        
        time += 1

    return time

if __name__ == "__main__":
    n, w, L = map(int, input().split())
    trucks = list(map(int, input().split()))

    print( cross_bridge(w, L, trucks) )