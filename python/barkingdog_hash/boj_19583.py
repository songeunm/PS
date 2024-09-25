# 싸이버개강총회
# hash

import sys
input = sys.stdin.readline

def to_seconds(t: str):
    m, s = map(int, t.split(':'))
    return m * 60 + s

if __name__ == "__main__":
    s, e, q = input().split()
    s_sec = to_seconds(s)
    e_sec = to_seconds(e)
    q_sec = to_seconds(q)

    names = set()
    count = 0
    while 1:
        try:
            t, name = input().split()
            t_sec = to_seconds(t)
            # 입장 체크
            if t_sec <= s_sec:
                names.add(name)
            # 퇴장 체크
            elif e_sec <= t_sec <= q_sec:
                if name in names:
                    names.remove(name)
                    count += 1
        except Exception as e:
            # print(e)
            break
    
    print(count)
        