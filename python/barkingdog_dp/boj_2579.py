# 계단 오르기


import sys
input = sys.stdin.readline

def dp (steps: list):
    n = len(steps)
    max_scores = [0 for i in range(n)]
    if n < 3:
        return steps[-1]
    max_scores[0] = steps[0]
    max_scores[1] = steps[1]
    max_scores[2] = steps[1] + steps[2]

    for i in range(3, n):
        score = max(max_scores[i - 2], max_scores[i - 3] + steps[i - 1]) + steps[i]
        max_scores[i] = score
    # print(max_scores)
    return max_scores[-1]


if __name__ == "__main__":
    s = int(input())
    steps = [0]
    for step in range(s):
        score = int(input())
        steps.append(score)
    
    result = dp(steps)
    print(result)