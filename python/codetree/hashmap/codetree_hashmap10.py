# 특별한 문자

import sys
from collections import defaultdict

input = sys.stdin.readline

if __name__ == "__main__":
    string = input().rstrip()
    
    dd = defaultdict(int)
    for s in string:
        dd[s] += 1
    
    answer = None
    for key in dd:
        if dd[key] == 1:
            answer = key
            break
    print()