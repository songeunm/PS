# 자두나무
# dp

import sys
input = sys.stdin.readline

def dp (plum: list, w: int):
    t = len(plum)
    # memo[i][j]: i번째 자두가 떨어질 때 이동을 j번 한 경우 받은 최대 자두 수
    memo = [[-1 for i in range(w + 1)] for i in range(t)]
    
    if plum[0] == 1:
        m_0 = [1, 0]
    else:
        m_0 = [0, 1]
    m_0.extend([-1 for i in range(w - 1)])
    memo[0] = m_0

    for i in range(1, t):
        for j in range(0, w + 1):
            # print(f"Calculating memo[{i}][{j}]")
            if j == 0:
                if plum[i] == 1:
                    memo[i][j] = memo[i - 1][j] + 1
                else:
                    memo[i][j] = memo[i - 1][j]
                # print(f"  No move: memo[{i}][{j}] = {memo[i][j]}")
                continue
            # j(이동한 횟수)가 짝수면 1번 나무에 있는 것
            if j % 2 + 1 == plum[i]:
                val_1 = memo[i - 1][j - 1] + 1
                val_2 = memo[i - 1][j] + 1
            else:
                val_1 = memo[i - 1][j - 1]
                val_2 = memo[i - 1][j]
            memo[i][j] = max(val_1, val_2)
            # print(f"  memo[{i}][{j}] = max({val_1}, {val_2}) = {memo[i][j]}")
    # print(*memo)
    return max(memo[-1])


if __name__ == "__main__":
    t, w = map(int, input().split())

    plum = []
    for drop in range(t):
        num = int(input())
        plum.append(num)
    
    result = dp(plum, w)
    print(result)