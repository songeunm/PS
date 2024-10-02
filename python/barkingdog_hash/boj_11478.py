# 서로 다른 부분 문자열의 개수
# hash

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    s = input().rstrip()
    parts = set()
    for l in range(1, len(s)+1):
        idx = 0
        while idx+l <= len(s):
            parts.add(s[idx: idx+l])
            idx += 1
    print(len(parts))