# 암호 만들기

import sys
input = sys.stdin.readline

# c개의 문자중에서 조건을 만족하는 l개를 뽑는 모든 경우 (정렬)
# 최소 모음 1개 자음 2개
# 3 ≤ L, C ≤ 15

lst = []

def bt(apv: list, condition: list):
    # condition = [선택해야하는 전체 문자 수, 선택해야하는 남은 모음 수, 선택해야하는 남은 자음 수]
    if condition[0] <= 0:
        if condition[1] == 0 and condition[2] == 0:
            print("".join(lst))
        return

    for i in range(len(apv)):
        lst.append(apv[i])
        if apv[i] in "aeiou":
            # print(f"{apv[i]} - {lst} - {condition} 모음")
            cond_1 = condition[1] - 1 if condition[1] >= 1 else 0
            # print(f"    {[condition[0]-1, cond_1, condition[2]]}")
            bt(apv[i+1:], [condition[0]-1, cond_1, condition[2]])
        else:
            # print(f"{apv[i]} - {lst} - {condition} 자음")
            cond_2 = condition[2] -1 if condition[2] >= 1 else 0
            # print(f"    {[condition[0]-1, condition[1], cond_2]}")
            bt(apv[i+1:], [condition[0]-1, condition[1], cond_2])
        lst.pop()


if __name__ == "__main__":
    l, c = map(int, input().split())
    apv = input().split()

    apv.sort()
    bt(apv, [l, 1, 2])
