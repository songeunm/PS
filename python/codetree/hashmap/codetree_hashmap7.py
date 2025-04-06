# 자주 등장한 top K 숫자

import sys
from collections import defaultdict

input = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    freq = defaultdict(int)
    for num in nums:
        freq[num] += 1
    print(* sorted(freq.keys(), key=lambda x: (freq[x], x), reverse=True)[:k])