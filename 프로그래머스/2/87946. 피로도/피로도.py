from itertools import permutations

def solution(k, dungeons):
    answer = 0

    for order in permutations(dungeons): 
        ans = 0 
        tmp = k 

        for under, use in order: 
            if tmp >= under:
                tmp -= use
                ans += 1

        if ans > answer:
            answer = ans
    return answer
