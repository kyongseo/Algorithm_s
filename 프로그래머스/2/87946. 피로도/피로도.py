from itertools import permutations

def solution(k, dungeons):
    
    answer = 0 
    for dun in permutations(dungeons):
        count = k
        ans = 0
        for order, use in dun:
            if count >= order:
                count -= use
                ans += 1
                
        if ans > answer:
            answer = ans
    return answer
