def solution(s):
    answer = s.split(" ")
    
    for i in range(len(answer)):
        answer[i] = answer[i][:1].upper() + answer[i][1:].lower()
    return ' '.join(answer)

