# K진 트리
# LCA - Binary Lifting

import sys
input = sys.stdin.readline

def get_parent(k, x):
    if x == 1:
        return 1
    else:
        return (x - 2) // k + 1

def get_distance(k, x, y):
    result = 0
    if k == 1:
        return abs(x - y)
    while x != y:
        if x > y:
            x = get_parent(k, x)
        else:
            y = get_parent(k, y)
        result += 1
    return result

if __name__ == "__main__":
    n, k, q = map(int, input().split())
    for _ in range(q):
        x, y = map(int, input().split())
        answer = get_distance(k, x, y)
        print(answer)