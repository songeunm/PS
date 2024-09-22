# 수강신청
# hash

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    k, l = map(int, input().split())
    line = {}
    for i in range(l):
        student_num = input().rstrip()
        line[student_num] = i
    
    sorted_line = sorted(line, key=lambda x: line[x])
    i = 0
    while i < k and i < len(sorted_line):
        print(sorted_line[i])
        i += 1
