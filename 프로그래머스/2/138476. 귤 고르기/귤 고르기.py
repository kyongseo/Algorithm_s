from collections import Counter

def solution(k, tangerine):
    answer = 0

    for c in Counter(tangerine).most_common():
        k -= c[1] 

        answer += 1

        if k <= 0:
            break

    return answer