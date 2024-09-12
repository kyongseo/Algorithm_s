def solution(want, number, discount):
    
    cnt = 0
    s = []
    for i in range(len(want)):
        for j in range(number[i]):
            s.append(want[i])
        s. sort()
        
    for i in range(len(discount) - 9):
        list_10 = discount[i:i+10]
        list_10.sort()
    
        if s == list_10:
            cnt += 1

    return cnt