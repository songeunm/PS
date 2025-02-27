# 체육복

# greedy

def solution(n, lost, reserve):
    student = [1 for i in range(n + 1)]
    for i in lost:
        student[i] -= 1
    for i in reserve:
        student[i] += 1

    answer = sum(map(lambda x: x > 0, student)) - 1
    for i in range(1, n + 1):
        if student[i] == 2 and student[i - 1] == 0:
            student[i] = 1
            student[i - 1] = 1
            answer += 1
        elif student[i] == 0 and student[i - 1] == 2:
            student[i] = 1
            student[i - 1] = 1
            answer += 1
    return answer