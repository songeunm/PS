# 시리얼 번호

import sys

# 길이 -> 짧은것 부터
# 숫자 자릿수합 -> 작은것 부터
# 사전순 (숫자 -> 알파벳)

# N ≤ 50 
# 시리얼 번호 최대 길이 = 50

# merge sort
def custom_compare(sn1: str, sn2: str):
    if len(sn1) < len(sn2):
        return (sn1, sn2)
    elif len(sn1) > len(sn2):
        return (sn2, sn1)
    else:
        sum_sn = [0, 0]
        for i, sn in [(0, sn1), (1, sn2)]:
            for x in sn:
                try:
                    sum_sn[i] += int(x)
                except:
                    sum_sn[i] += 0
        if sum_sn[0] < sum_sn[1]:
            return (sn1, sn2)
        elif sum_sn[0] > sum_sn[1]:
            return (sn2, sn1)
        else:
            if sn1 < sn2:
                return (sn1, sn2)
            elif sn1 > sn2:
                return (sn2, sn1)
            else:
                return 0 # 잘못된 입력

def merge_part(part1: list, part2: list):
    result = []
    i, j = 0, 0
    while i < len(part1) or j < len(part2):
        if i >= len(part1):
            result.append(part2[j])
            j += 1
            continue
        if j >= len(part2):
            result.append(part1[i])
            i += 1
            continue
        if custom_compare(part1[i], part2[j]) == (part1[i], part2[j]):
            result.append(part1[i])
            i += 1
        else:
            result.append(part2[j])
            j += 1
    return result

def merge_sort(sn: list):
    while len(sn) > 1:
        result = []
        for i in range(0, len(sn)-1, 2):
            result.append(merge_part(sn[i], sn[i+1]))
        if len(sn) % 2 == 1:
            result.append(sn[-1])
        # print(f"sorting ... : {result}")
        sn = result
    return sn


if __name__ == "__main__":
    n = int(input())
    sn = [[input()] for i in range(n)]
    result = merge_sort(sn)
    print('\n'.join(result[0]))