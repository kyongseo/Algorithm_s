def solution(elements):
    el = elements + elements
    n = len(elements) 
    answ = set()
    
    for i in range(1, n + 1):
        for j in range(n):
            to = sum(el[j:j+i])
            answ.add(to)
            
    return len(answ)