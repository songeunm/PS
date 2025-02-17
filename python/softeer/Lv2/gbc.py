# GBC
# lv. 2

import sys

input = sys.stdin.readline

def CompareSpeed(real_ev, test_ev):
    i, j = 0, 0
    max_value = 0
    while i < len(real_ev) and j < len(test_ev):
        max_value = max(max_value, test_ev[j][1] - real_ev[i][1])
        if real_ev[i][0] < test_ev[j][0]:
            # print(f"now {real_ev[i][0]} test {test_ev[j][1]} real {real_ev[i][1]}, {max_value}")
            i += 1
        elif real_ev[i][0] > test_ev[j][0]:
            # print(f"now {test_ev[j][0]} test {test_ev[j][1]} real {real_ev[i][1]}, {max_value}")
            j += 1
        else:
            # print(f"now {test_ev[j][0]} test {test_ev[j][1]} real {real_ev[i][1]}, {max_value}")
            i += 1
            j += 1
    return max_value
            

if __name__ == "__main__":
    n, m = map(int, input().split())
    
    real_ev = []
    hight = 0
    for _ in range(n):
        r, s = map(int, input().split())
        hight += r
        real_ev.append([hight, s])
        
    test_ev = []
    hight = 0
    for _ in range(m):
        r, s = map(int, input().split())
        hight += r
        test_ev.append([hight, s])

    # print(real_ev)
    # print(test_ev)

    result = CompareSpeed(real_ev, test_ev)
    print(result)