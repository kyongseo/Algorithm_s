def solution(babbling):
    answer = 0
    word = ["aya", "ye", "woo", "ma"]
    
    for b in babbling:
        for w in word:
            b = b.replace(w, ' ')
        b = b.replace(' ', '')
        if len(b) == 0:
            answer += 1
    return answer