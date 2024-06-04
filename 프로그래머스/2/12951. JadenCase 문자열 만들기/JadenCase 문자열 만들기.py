def solution(s):
    answer = s.split(" ")
    
    for i in range(0, len(answer)):
        answer[i] = answer[i][:1].upper() + answer[i][1:].lower()
    return ' '.join(answer)

