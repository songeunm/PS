# 패션왕 신해빈
# hash

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        closet = {}
        for i in range(n):
            name, category = input().split()
            # 착용하지 않는 경우의 수 +1
            closet[category] = closet.get(category, 1) + 1
        
        answer = 1
        for key, item in closet.items():
            answer *= item
        
        # 모든 의상을 입지 않는 경우의 수 -1
        print(answer-1)