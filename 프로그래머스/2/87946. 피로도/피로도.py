from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    for order in permutations(dungeons): #6
        ans = 0 
        tmp = k # 80
        
        for under, use in order: # 80, 20
            if tmp >= under:
                tmp -= use
                ans += 1

        if ans > answer:
            answer = ans
    return answer