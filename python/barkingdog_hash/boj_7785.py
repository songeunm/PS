# 회사에 있는 사람
# hash

import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    log = set()
    for i in range(n):
        name, status = input().split()
        
        if name in log:
            log.remove(name)
        else:
            log.add(name)
    answer = '\n'.join(sorted(list(log), reverse=True))
    print(answer)
