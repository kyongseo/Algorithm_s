def solution(babbling):
    answer = 0
    
    for ba in babbling:
        if check(ba):
            answer += 1
    return answer

def check(s):
    if len(s) == 0:
        return True
    if len(s) == 1:
        return False
    if s[:2] == "ye" or s[:2] == "ma":
        return check(s[2:])
    elif s[:3] == "aya" or s[:3] == "woo":
        return check(s[3:])
    return False