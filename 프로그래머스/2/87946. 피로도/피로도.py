from itertools import permutations

def solution(k, dungeons):
    answer = 0 

    for dun in permutations(dungeons):

        ans = 0
        tmp = k
        for min, use in dun:
            if tmp >= min:
                tmp -= use
                ans += 1
        if ans > answer:
            answer = ans

    return answer

