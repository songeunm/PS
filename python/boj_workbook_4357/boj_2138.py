"""
전구와 스위치
greedy
"""

import sys
from copy import deepcopy

input = sys.stdin.readline

# greedy algorithm

def switch(now: list, switch_idx: int):
    on_off = lambda x: '0' if x=='1' else '1'
    now[switch_idx] = on_off(now[switch_idx])
    if switch_idx-1 >= 0:
        now[switch_idx-1] = on_off(now[switch_idx-1])
    if switch_idx+1 < len(now):
        now[switch_idx+1] = on_off(now[switch_idx+1])
    return now

def bulb(now, target):
    N = len(now)
    times = 0

#    print(f"now: {now}")
    for i in range(1,N):
        if now[i-1] != target[i-1]:
            switch(now, i)
            times += 1
        else:
            pass
#        print(f"now: {now}, target: {target}")
    
    if ''.join(now) == ''.join(target):
        return times
    else:
        return float('inf')


if __name__ == "__main__":
    N = int(input())
    now = list(input().rstrip())
    target = list(input().rstrip())

    now1 = deepcopy(now)
    res1 = bulb(now1, target) # dont push 1st switch
    now2 = deepcopy(now)
    res2 = bulb(switch(now2, 0), target) + 1 # push 1st switch
    res = min(res1, res2)
    if res == float('inf'):
        print(-1)
    else:
        print(res)