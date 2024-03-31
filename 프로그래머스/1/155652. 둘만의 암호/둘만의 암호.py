def solution(s, skip, index):
    alp = "abcdefghijklmnopqrstuvwxyz" #26
    answer = ""
    for i in list(skip):
        alp = alp.replace(i,"") #acefg... bd
        
    for a in s:
        answer += alp[(alp.find(a) + index) % len(alp)] #21
    return answer