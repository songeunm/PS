"""
괄호 추가하기 3
브루트포스, dp
"""

import sys
import re

input = sys.stdin.readline

def max_calc(exp: list):
    while 1:
        # 0이 곱해진 항 0 으로 변경
        new_exp = re.sub('\d\*0\*\d|\d\*0|0\*\d', '0', exp)
        if exp == new_exp:
            break
        else:
            exp = new_exp

    nums = []
    opr = ''
    i = 0
    while i < len(exp):
        e = exp[i]
#        print(e)
        if e == '+':
            # + 연산자의 경우
            # now 계산
            i += 1
            nums.append(nums.pop() + int(exp[i]) )
        elif e == '-':
            # - 연산자의 경우
            # opr - 이면 now 계산
            # 아니면: before 계산
            if opr=='-':
                i += 1
                nums.append(nums.pop() - int(exp[i]))
            elif len(nums)>1:
                if opr == '*':
                    nums.append(nums.pop() * nums.pop())
                else:
                    num2 = nums.pop()
                    num1 = nums.pop()
                    nums.append(num1 - num2)
                opr = '-'
                i += 1
                nums.append(int(exp[i]))
            else:
                opr = '-'
                i += 1
                nums.append(int(exp[i]))
        elif e == '*':
            # * 연산자의 경우
            # before 계산
            if len(nums)>1:
                if opr == '*':
                    nums.append(nums.pop() * nums.pop())
                else:
                    num2 = nums.pop()
                    num1 = nums.pop()
                    nums.append(num1 - num2)
            opr = '*'
            i += 1
            nums.append(int(exp[i]))
        else:
            # 숫자인 경우
            # nums
            nums.append(int(e))
        i += 1
#        print(f"nums: {nums}, opr: {opr}")

    if len(nums) > 1:
        if opr == '*':
            nums.append(nums.pop() * nums.pop())
        else:
            num2 = nums.pop()
            num1 = nums.pop()
            nums.append(num1 - num2)
    
    res = nums.pop()
    res = min(max(res, -2**31), 2**31)
    return res


if __name__ == "__main__":
    n = int(input())
    exp = input().rstrip()

    print( max_calc(exp) )



3 + 8 -> 11
3 + 8 * 7 -> 11 * 7
3 + 8 * 7 - 9 -> 77 - 9
3 + 8 * 7 - 9 * 2 -> 77 - 9
=> 136

3 + 8 * 7 - 9 * 2
3 + 8 => 11
11 * 7 => 11 * 7 (*)
11 * 7 - 9 (*) => 77 - 9 (-)
77 - 9 * 2 (-) => 68 * 2 (*)
=> 68 * 2 = 136



"작은 문제가 반복된다"
0) 식에 *0이 포함된 경우 해당 항의 값을 0으로 먼저 계산
1) +는 이전 수를 증가시키며 이후 어떤 연산이 와도 당장 계산하는게 최대이므로 바로 한다.
2) *는 이전 수를 증가시키지만 곱해지는 수가 더 커질 수 있으므로 keep 한다.
3) *는 지금 계산은 keep하고, 이전 계산은 어떤 연산이 와도 지금 계산보다 먼저 실행되는 것이 낫다.
    3-1) 이전 계산이 +라면 이미 계산되었을 것임
    3-2) 이전 계산이 -라면 빼지는 수가 곱셈으로 인해 더 커지기 전에 실행되는게 나음
    3-3) 이전 계산이 *라면 순서에 의미가 사라지므로 지금 하는게 나음
4) -는 이전 계산이 -인 경우 지금 계산을 진행해 빼지는 수를 감소시키도록 한다.
5) -는 이전 계산이 없거나 -가 아닌 경우 빼지는 수가 작아질 수 있으므로 지금 계산을 keep 한다. 

1 - 9 - 1 - 9 - 1 - 9 - 1 - 9 - 1 - 9
1 - 9 => 1 - 9 (-)
1 - 9 - 1 => 1 - 8 (-)
1 - 8 - 9 = > 1 - -1 (-)
1 - -1 - 1 =>  1 - -2 (-)
1 - -2 -9 => 1 - -11 (-)
1 - -11 -1 => 1 - -12 (-)
1 - -12 -9 => 1 - -21 (-)
1 - -21 -1 => 1 - -22 (-)
1 - 22 - 9 => 1 - -31 (-)
=> 32

from copy import deepcopy

test1 = '1*2+3*4*5-6*7*8*9*0'
test2 = '1*2+3*4*5-6*7*0*8*9'
test3 = '1*2+3*4*5-0*6*7*8*9'

test = deepcopy(test2)
test

test
