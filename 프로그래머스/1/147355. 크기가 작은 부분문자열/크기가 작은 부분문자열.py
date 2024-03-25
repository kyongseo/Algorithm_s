def solution(t, p):
    answer = 0
    p_len = len(p) # 3 
    t_len = len(t) # 7
    
    p = int(p) # 271
    for i in range(0,t_len+1-p_len): # 0,1,2,3,4
        if int(t[i:i+p_len]) <= p: 
            answer+=1
    return answer