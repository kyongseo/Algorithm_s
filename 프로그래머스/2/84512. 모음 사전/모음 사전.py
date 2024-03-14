from itertools import product

def solution(word):
    answer = 0
    
    result = list()
    for i in range(1, 6):
        li = list(product(["A", "E", "I", "O", "U"], repeat=i))
        for j in li:
            result.append(''.join(k for k in j))
        
    result.sort()
    answer = result.index(word) + 1

    return answer