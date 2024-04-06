def solution(d, budget):
    answer = 0    
    d.sort()
    now=0
    for x in d:
        if (now+x)<=budget:
            now+=x
            answer+=1
        else:
            break
    return answer