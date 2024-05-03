def solution(n, s):
    answer = []
    
    if s<n:
        return [-1]
    
    num = s//n
    rest = s%n
    
    for idx in range(n):
        answer.append(num)
    
    if rest != 0:
        for a in range(len(answer)):
            answer[a] += 1
            rest -= 1
            if rest == 0:
                break
    
    answer.sort()
    return answer