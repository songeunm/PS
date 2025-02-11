# 전광판
# lv. 2

import sys

input = sys.stdin.readline

number_to_bulb = {'0': 0b1110111,
                  '1': 0b0010010,
                  '2': 0b1011101,
                  '3': 0b1011011,
                  '4': 0b0111010,
                  '5': 0b1101011,
                  '6': 0b1101111,
                  '7': 0b1110010,
                  '8': 0b1111111,
                  '9': 0b1111011,
                  ' ': 0b0000000,}

def change_number(a, b):
    # if 5 - len(a) > 0:
    #     a = ' ' * (5 - len(a)) + a
    # if 5 - len(b) > 0:
    #     b = ' ' * (5 - len(b)) + b
    ## => .rjust를 통해 정렬함으로써 깔끔하게 표현 가능
    a = a.rjust(5, ' ')
    b = b.rjust(5, ' ')

    count = 0
    for i in range(5):
        a_bulb = number_to_bulb[a[i]]
        b_bulb = number_to_bulb[b[i]]
        calc = bin(a_bulb ^ b_bulb)
        # switch = sum(map(int, list(calc[2:])))
        # count += switch
        ## => .count()를 사용하여 더 직관적으로 표현
        count += calc.count('1')
    return count
    

if __name__ == "__main__":
    t = int(input())
    for testcase in range(t):
        a, b = input().split()
        result = change_number(a, b)
        print(result)