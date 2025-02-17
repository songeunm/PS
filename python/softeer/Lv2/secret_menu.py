# 비밀 메뉴
# lv. 2

import sys

input = sys.stdin.readline

if __name__ == "__main__":
    m, n, k = map(int, input().split())
    secret = "".join(input().rstrip())
    action = "".join(input().rstrip())

    if action.find(secret) >= 0:
        print("secret")
    else:
        print("normal")