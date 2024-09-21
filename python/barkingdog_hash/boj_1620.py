# 나는야 포켓몬 마스터 이다솜
# hash

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())
    names = {}
    numbers = {}
    for i in range(n):
        name = input().rstrip()
        names[name] = i+1
        numbers[i+1] = name
    for i in range(m):
        quize = input().rstrip()
        try:
            number = int(quize)
            print(numbers[number])
        except:
            print(names[quize])
