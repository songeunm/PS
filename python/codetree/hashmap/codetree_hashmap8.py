# 원소의 합이 0

import sys
from collections import defaultdict

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    seq = {keys: [] for keys in ['a', 'b', 'c', 'd']}
    for key in seq.keys():
        seq[key] = list(map(int, input().split()))
    
    comb1 = defaultdict(int)
    for num in seq['a']:
        comb1[num] += 1
    comb2 = defaultdict(int)
    for num1 in seq['b']:
        for num2 in comb1:
            comb2[num1 + num2] += comb1[num2]

    comb3 = defaultdict(int)
    for num in seq['c']:
        comb3[num] += 1
    comb4 = defaultdict(int)
    for num1 in seq['d']:
        for num2 in comb3:
            comb4[num1 + num2] += comb3[num2]

    answer = 0
    for num in comb2:
        target = -num
        answer += comb2[num] * comb4.get(target, 0)
    print(answer)