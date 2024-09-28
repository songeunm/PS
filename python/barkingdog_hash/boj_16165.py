# 걸그룹 마스터 준석이
# hash

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())

    group_key = {}
    member_key = {}
    for i in range(n):
        team = input().rstrip()
        number = int(input())
        for num in range(number):
            member = input().rstrip()
            group_key[team] = group_key.get(team, []) + [member]
            member_key[member] = team

    # print(group_key)
    # print(member_key)

    for i in range(m):
        quize = input().rstrip()
        q_type = int(input())
        if q_type:
            print(member_key[quize])
        else:
            for member in sorted(group_key[quize]):
                print(member)