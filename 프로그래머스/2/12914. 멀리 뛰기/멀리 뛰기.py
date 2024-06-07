def solution(n):
    cnt = 0
    check = {}
    check[1] =1
    check[2] =2
    for i in range(3, n+1):
        check[i] = check[i-2] + check[i-1]
    cnt = check[n] % 1234567
    return cnt