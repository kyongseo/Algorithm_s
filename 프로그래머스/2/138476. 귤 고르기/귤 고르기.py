from collections import Counter

def solution(k, tangerine):
    answer = 0
    for irr in Counter(tangerine).most_common():
        k -= irr[1]
        answer += 1

        if k <= 0:
            break
    return answer