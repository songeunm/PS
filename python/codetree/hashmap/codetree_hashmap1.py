# hashmap 기본

import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input()) # 1 <= n <= 100,000
    dictionary = {}
    for _ in range(n):
        inp = input().split()
        cmd = inp[0]
        if cmd == "add":
            num1 = inp[1]
            num2 = inp[2]
            dictionary[num1] = num2
        elif cmd == "remove":
            num = inp[1]
            dictionary.pop(num)
        else:
            try:
                num = inp[1]
                print(dictionary[num])
            except:
                print(None)