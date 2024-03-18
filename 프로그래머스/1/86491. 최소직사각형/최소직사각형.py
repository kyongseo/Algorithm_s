def solution(sizes):
    w = [] # 가로 값을 담을 빈 리스트 생성
    h = [] # 세로 값
    for i in range(len(sizes)): # sizes는 2차원 리스트
        
        if sizes[i][0] >= sizes[i][1]: # 조건 : 가로>=세로
            
            w.append(sizes[i][0]) 
            h.append(sizes[i][1]) 
            
        else: # 명함번호2 해당
            h.append(sizes[i][0]) 
            w.append(sizes[i][1]) 

    return max(w) * max(h)