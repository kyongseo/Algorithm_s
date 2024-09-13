def solution(arr1, arr2):
    
    m = len(arr1) # 행의 수 
    n = len(arr1[0]) # 열의 수
    p = len(arr2[0]) # 열의 수 
    
    
    answer = [[0] * p for _ in range(m)]
    
    for m2 in range(m):
        for n2 in range(n):
            for p2 in range(p):
                answer[m2][p2] +=  arr1[m2][n2] * arr2[n2][p2]
    return answer