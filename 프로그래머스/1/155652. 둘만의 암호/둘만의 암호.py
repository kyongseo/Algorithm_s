def solution(s, skip, index):
    alp = "abcdefghijklmnopqrstuvwxyz"
    answer = ""
    for i in list(skip):
        alp = alp.replace(i,"")
        
    for a in s:
        answer += alp[(alp.find(a) + index) % len(alp)]
    return answer