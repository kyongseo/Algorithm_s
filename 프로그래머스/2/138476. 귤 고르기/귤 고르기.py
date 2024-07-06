from collections import Counter as c

def solution(k, tangerine):
    answer = 0 
    for arr in c(tangerine).most_common():
        
        k -= arr[1]
        answer += 1

        if k <= 0:
            break
            
    return answer