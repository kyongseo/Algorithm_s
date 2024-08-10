def solution(n, left, right):
    answer = []
    # 규칙 :: 인덱스를 확인하기!
    for i in range(left, right+1):
        a = i//n 
        b = i % n
        if a < b:
            a,b = b,a
        answer.append(a+1)
        
    return answer