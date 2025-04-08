# 순서를 바꾸었을 때 같은 단어 그룹화하기

import sys
from collections import defaultdict

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())

    group = defaultdict(int)
    for _ in range(n):
        word = input().rstrip()
        elements = defaultdict(int)
        for w in word:
            elements[w] += 1
        group_key = ""
        for key in sorted(elements.keys()):
            group_key += key + str(elements[key])
        group[group_key] += 1
    
    answer = 0
    for gk in group:
        if answer < group[gk]:
            answer = group[gk]
    print(answer)

# ----------------------------------------------- 개선
import sys
from collections import defaultdict

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())

    group = defaultdict(int)
    for _ in range(n):
        word = str(sorted(list(input().rstrip()))) # 애초에 정렬해버리기
        group[word] += 1
    
    answer = 0
    for gk in group:
        if answer < group[gk]:
            answer = group[gk]
    print(answer)