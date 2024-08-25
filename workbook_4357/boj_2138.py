import sys
from itertools import combinations

input = sys.stdin.readline
sys.setrecursionlimit(100000)

# greedy algorithm

def switch(now: list, switch_idx: int):
    on_off = lambda x: '0' if x=='1' else '1'
    now[switch_idx] = on_off(now[switch_idx])
    if switch_idx-1 >= 0:
        now[switch_idx-1] = on_off(now[switch_idx-1])
    if switch_idx+1 < len(now):
        now[switch_idx+1] = on_off(now[switch_idx+1])
    return now

def bulb(now: list, target: list, times: int, idx: int, button: list):
    N = len(now)

    if ''.join(now) == ''.join(target):
#        print(button)
        return times
    elif idx >= N:
        return -1
    else:
        if idx==0:
            res1 = bulb(now, target, times, idx+1, button) # no switch
            if res1 != -1:
                return res1
            res2 = bulb(switch(now, idx), target, times+1, idx+1, button+[idx]) # switch
            switch(now, idx)
            if res2 != -1:
                return res2
        else:
            if now[idx-1] == target[idx-1]:
                res = bulb(now, target, times, idx+1, button) # no switch
            else:
                res = bulb(switch(now, idx), target, times+1, idx+1, button+[idx]) # switch
                switch(now, idx)
    
    return res


if __name__ == "__main__":
    N = int(input())
    now = list(input().rstrip())
    target = list(input().rstrip())

    print(bulb(now, target, 0, 0, []))