# +=
# dp

T = int(input())
for test_case in range(1, T + 1):
    a, b, n = map(int, input().split())
    max_val = max(a, b)
    min_val = min(a, b)
    
    val = a + b
    cnt = 1
    # fibonacci
    num1 = 1 # max_val 계수
    num2 = 1 # min_val 계수
    
    while val <= n:
        tmp = num1
        num1 += num2
        num2 = tmp
        val = num1 * max_val + num2 * min_val
        cnt += 1
    print(cnt)