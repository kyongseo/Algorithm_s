def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)): #0,1,2
        if signs[i]: # 4, 12
            answer += absolutes[i] # 4+ 12
        else: # -7
            answer -= absolutes[i] # -7
    return answer
